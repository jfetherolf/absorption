import numpy as np

from pyrho import ham, redfield, spec

def main(omega_c, beta):
    nsite = 2
    nbath = 1

    eps = 0.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ eps, 0.],
                        [0., eps]])

    # System part of the the system-bath interaction
    ham_sysbath = []
    for n in range(1,nsite):
        ham_sysbath_n = np.zeros((nsite,nsite))
        ham_sysbath_n[n,n] = 1.0
        ham_sysbath.append( ham_sysbath_n )

    rho_g = np.zeros((nsite,nsite))
    rho_g[0,0] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.],
                       [ 1.,  0.]])
                       
        
    for omega_c in [omega_c]:
        for beta in [beta]:
            for method in ['Redfield','TCL2']:
                
                t_final = 300.
                dt = 0.01
                lamda = 0.5
                kT = 1./beta
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                my_redfield = redfield.Redfield(my_ham, method=method)

#               time, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)
              
                my_spec = spec.Spectroscopy(dipole, my_redfield)
                omegas, intensities = my_spec.absorption(-4.+eps, 4.+eps, 0.02, rho_g, t_final, dt, dipole_file = 'dipole_omegac%0.1f_beta%0.1f_%s.dat'%(omega_c,beta,method), is_damped=True)

                with open('abs_omegac%0.1f_beta%0.1f_lamda%0.1f_%s.dat'%(omega_c,beta,lamda,method), 'w') as f:
                    for (omega, intensity) in zip(omegas, intensities):
                        f.write('%0.8f %0.8f\n'%(omega-eps, intensity))

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) != 2:
        print 'usage: run'
        sys.exit(1)
    omega_c = float(args[0])
    beta = float(args[1])
    main(omega_c, beta)
