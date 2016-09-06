import numpy as np

from pyrho import ham, redfield, spec

def main():
    nsite = 1+2
    nbath = 2
    
    kB = 0.69352    # in cm-1 / K
    kT = kB*300.
    hbar = 5308.8   # in cm-1 * fs

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ 0.,  0.,  0.],
                        [ 0., 100.,100.],
                        [ 0., 100., 0.]])

    # System part of the the system-bath interaction
    ham_sysbath = []
    for n in range(1,nsite):
        ham_sysbath_n = np.zeros((nsite,nsite))
        ham_sysbath_n[n,n] = 1.0
        ham_sysbath.append( ham_sysbath_n )

    rho_g = np.zeros((nsite,nsite))
    rho_g[1,1] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1.],
                       [ 1.,  0.,  0.],
                       [ 1.,  0.,  0.]])

        
    for omega_c in [1./100.]:
        for beta in [1./kT]:
        
#               t_init = 0.0
            t_final = 1000.
            dt = 0.5
            lamda = 100.
            kT = 1./beta
            spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

            my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, hbar=hbar)
            
            my_redfield = redfield.Redfield(my_ham, method='TCL2')

#               times, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)

            my_spec = spec.Spectroscopy(dipole, my_redfield)
            omegas, intensities = my_spec.absorption(-900., 1000., 0.02, rho_g, t_final, dt, dipole_file =
                    'dipole_eet_redfm_noPD_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), is_damped=True)

#               with open('pop_eet_redfm_noPD_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), 'w') as f:
#                   for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
#                       f.write('%0.8f %0.8f %0.8f\n'%(time, rho_site[1,1].real, rho_site[2,2].real))


            with open('eet_tcl2_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), 'w') as f:
                for (omega, intensity) in zip(omegas, intensities):
                    f.write('%0.8f %0.8f\n'%(omega-100, intensity))


if __name__ == '__main__':
    main()
