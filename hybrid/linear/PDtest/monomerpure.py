import numpy as np

from pyrho import ham, redfield, spec

def main():
    nsite = 1+1
    nbath = 1

    eps = 0.
    hbar = 1.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ 0.,  0.],
                        [ 0., eps]])

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

        
    for omega_c in [1000.]:
        for beta in [1.]:
            for method in ['TCL2','Redfield']:
                t_final = 1000.
                dt = 0.1
                lamda = 0.5
                kT = 1./beta
                
                spec_density_1 = [['ohmic-lorentz', lamda, omega_c]]*nbath
                spec_density_2 = [['ohmic-lorentz', lamda, omega_c]]*nbath


                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_density_1, kT)
                
                my_redfield = redfield.Redfield(my_ham, method=method)


    #               time, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)

                my_spec = spec.Spectroscopy(dipole, my_redfield)
                omegas, intensities = my_spec.absorption(-4.+eps, 4.+eps, 0.02, rho_g, t_final, dt, dipole_file =
                        'dipole_hybrid_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), is_damped=True)

                with open('abs_pure_%s_omegac%0.1f_beta%0.1f.dat'%(method,omega_c,beta), 'w') as f:
                    for (omega, intensity) in zip(omegas, intensities):
                        f.write('%0.8f %0.8f\n'%(omega-eps, intensity))

if __name__ == '__main__':
    main()
