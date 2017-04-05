import sys
import numpy as np

from pyrho import ham,redfield, spec

def main(omega_c, beta):
    nsite = 1+2
    nbath = 2

    eps = 0.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ 0.,  0.,  0.],
                        [ 0., eps,  1.],
                        [ 0., 1., -eps]])

    # System part of the the system-bath interaction
    ham_sysbath = []
    for n in range(1,nsite):
        ham_sysbath_n = np.zeros((nsite,nsite))
        ham_sysbath_n[n,n] = 1.0
        ham_sysbath.append( ham_sysbath_n )
    ham_sysbath_n[nsite-1,nsite-1] = 2.0
    rho_g = np.zeros((nsite,nsite))
    rho_g[1,1] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1.],
                       [ 1.,  0.,  0.],
                       [ 1.,  0.,  0.]])

        
    for omega_c in [omega_c]:
        for beta in [beta]:
            for nmode in [300]:
#               t_init = 0.0
                t_final = 30.
                dt = 0.05
                lamda = 5.0
                kT = 1./beta
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                my_redfield = redfield.Redfield(my_ham, method='TCL2')

                times, rhos_site,rhos_eig = my_redfield.propagate(rho_g, 0.0, t_final, dt)

                with open('pop_TCL2_weirdsysbath_2015_omegac-%0.1f_lam-%0.1f_beta-%0.1f.dat'%(omega_c,lamda,beta), 'w') as f:
                    for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                        f.write('%0.8f %0.8f\n'%(time, rho_site[0,0].real - rho_site[1,1].real))


    
    
    
    
if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 2:
        print 'usage: run'
        sys.exit(1)
    omega_c = float(args[0])
    beta = float(args[1])
    main(omega_c, beta)
