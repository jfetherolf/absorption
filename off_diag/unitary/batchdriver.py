import numpy as np

from pyrho import ham, unitary, spec

def main():
    nsite = 1+2
    nbath = 2+1
    
    eps = 4.

    # System Hamiltonian
    # n = 0 is ground state
    for V in [1.,2.,3.]:
        ham_sys = np.array([[ 0.,  0.,  0.],
                            [ 0., eps, -V],
                            [ 0., -V, -eps]])

        # System part of the the system-bath interaction
        ham_sysbath = []
        ham_sysbath.append(np.array([[ 0.,  0.,  0.],
                            [ 0., 0., 1.],
                            [ 0., 1., 0.]]))

        for n in range(1,nsite):
#           for m in range(1,nsite):
            ham_sysbath_n = np.zeros((nsite,nsite))
            ham_sysbath_n[n,n] = 1.0
            ham_sysbath.append( ham_sysbath_n )

#               if n!=m:
#                   ham_sysbath_n = np.zeros((nsite,nsite))
#                   ham_sysbath_n[n,m] = 1.0
#                   ham_sysbath.append( ham_sysbath_n )
#                else:
#                    ham_sysbath_n = np.zeros((nsite,nsite))
#                    ham_sysbath_n[n,m] = 0.0
#                    ham_sysbath.append( ham_sysbath_n )

        print ham_sysbath
        rho_g = np.zeros((nsite,nsite))
        rho_g[0,0] = 1.0

        # Dipole operator connecting the ground state to the excited states
        dipole = np.array([[ 0.,  1.,  1.],
                           [ 1.,  0.,  0.],
                           [ 1.,  0.,  0.]])

            
        for omega_c in [1.0]:
            for beta in [1.0]:
                t_final = 100.
                dt = 0.01
                lamda = 2.0
                kT = 1./beta
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                my_unitary = unitary.Unitary(my_ham)

#               time, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)

                my_spec = spec.Spectroscopy(dipole, my_unitary)
                omegas, intensities = my_spec.absorption(-10.+eps, 10.+eps, 0.05, rho_g, t_final, dt, dipole_file = 'dipole_unitary_V%0.1f.dat'%(V), is_damped=True)

            #   with open('abs_hybrid_redfield_fm_omegac%0.1f_beta%0.1f_split%0.1f_run%d.dat'%(omega_c,beta,omega_split[1],run), 'w') as f:
                with open('abs_unitary_V%0.2f.dat'%(V), 'w') as f:
                    for (omega, intensity) in zip(omegas, intensities):
                        f.write('%0.8f %0.8f\n'%(omega-eps, intensity))

if __name__ == '__main__':
    main()
