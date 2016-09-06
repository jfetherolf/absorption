import numpy as np

from pyrho import ham, frozen, redfield, hybrid, spec

def main():
    nsite = 1+2
    nbath = 2

    eps = 0.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ 0.,  0.,  0.],
                        [ 0., eps, -1.],
                        [ 0., -1., eps]])

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

        
    for omega_c in [0.3]:
        for beta in [1.]:
            for nmode in [300]:

                omega_r = 2*np.sqrt( (ham_sys[1,1]-ham_sys[2,2])**2 / 4.0 + ham_sys[1,2]**2 )
                
                omega_split = []

                for n in range(nbath):
                    omega_split.append(max(omega_r/4., omega_c))
#                   omega_split.append(1e16)


#               t_init = 0.0
                ntraj = int(1e3)
                t_final = 50.
                dt = 0.01
                lamda = 0.5
                kT = 1./beta
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                my_frozen = frozen.FrozenModes(my_ham_slow, nmode=nmode, ntraj=ntraj)
                my_redfield = redfield.Redfield(my_ham_fast, method='Redfield')

                my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split)

                times,rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)

                with open('hybrid_pop_site_omegac-%0.1f_beta-%0.2f.dat'%(omega_c,beta), 'w') as f:
                    for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                        f.write('%0.8f %0.8f %0.8f\n'%(time, rho_site[1,1].real, rho_site[2,2].real))



#               my_spec = spec.Spectroscopy(dipole, my_hybrid)
#               omegas, intensities = my_spec.absorption(-4.+eps, 4.+eps, 0.02, rho_g, t_final, dt)




#               with open('hybrid_omegac%0.1f_beta%0.1f_lamda%0.1f_test.dat'%(omega_c,beta,lamda), 'w') as f:
#                   for (omega, intensity) in zip(omegas, intensities):
#                       f.write('%0.8f %0.8f\n'%(omega-eps, intensity))

if __name__ == '__main__':
    main()
