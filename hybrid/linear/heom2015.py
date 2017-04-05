import sys
import numpy as np

from pyrho import ham, heom

def main():
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
    ham_sysbath_n[2,2] = 2.0
    rho_0 = np.zeros((nsite,nsite))
    rho_0[1,1] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1.],
                       [ 1.,  0.,  0.],
                       [ 1.,  0.,  0.]])



    for lamda in [5.00]: 
        for omega_c in [0.25]:
            for L in [21]: 
                t_final = 25.
                dt = 0.001
                beta = 0.5
                kT = 1./beta        
                
                # Spectral densities - a list of length 'nbath'
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                
                my_heom = heom.HEOM(my_ham, L=L, K=0)
                
                times, rhos_site, rhos_eig = my_heom.propagate(rho_0, 0.0, t_final, dt)
                    

                with open('pop_2015HEOM_weirdsysbath_omegac-%0.1f_lam-%0.1f_beta-%0.1f_L%d.dat'%(omega_c,lamda,beta,L), 'w') as f:
                    for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                        f.write('%0.8f %0.8f\n'%(time, rho_site[0,0].real - rho_site[1,1].real))

if __name__ == '__main__':
    main()
