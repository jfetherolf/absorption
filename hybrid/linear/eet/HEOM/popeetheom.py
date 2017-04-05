import numpy as np

from pyrho import ham, heom, spec

def main(tau_c, T, lamda, L):
    nsite = 1+2
    nbath = 2
    
    kB = 0.69352    # in cm-1 / K
    kT = kB*T
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

  # start at [1,1] for populations!
    rho_g = np.zeros((nsite,nsite))
    rho_g[1,1] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1.],
                       [ 1.,  0.,  0.],
                       [ 1.,  0.,  0.]])

        
    for omega_c in [1/tau_c]:
        for beta in [1./kT]:
            for lamda in [lamda]:
                for L in [L]:

                    t_final = 1000.
                    dt = 0.2
                    lamda = lamda
                    kT = 1./beta
                    spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, hbar=hbar)
                    

                    my_heom = heom.HEOM(my_ham, L=L, K=0)

                    times, rhos_site,rhos_eig = my_heom.propagate(rho_g, 0.0, t_final, dt)

    #               my_spec = spec.Spectroscopy(dipole, my_heom)
    #               omegas, intensities = my_spec.absorption(-900., 1100., 1., rho_g, t_final, dt, dipole_file =
    #                   'dipole_eet_heom_tauc%0.01f_T%0.01f_lamda%0.01f_L%d.dat'%(tau_c,T,lamda,L), is_damped=True)

                    with open('pop_eet_redfm_noPD_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), 'w') as f:
                        for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                            f.write('%0.8f %0.8f %0.8f\n'%(time, rho_site[1,1].real, rho_site[2,2].real))


    #               with open('eet_heom_tauc%0.01f_T%0.01f_lamda%0.01f_L%d_K1.dat'%(tau_c,T,lamda,L), 'w') as f:
    #                   for (omega, intensity) in zip(omegas, intensities):
    #                       f.write('%0.8f %0.8f\n'%(omega-100, intensity))

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) != 4:
        print 'usage: run'
        sys.exit(1)
    tau_c = float(args[0])
    T = float(args[1])
    lamda = float(args[2])
    L = int(args[3])
    main(tau_c, T, lamda, L)
