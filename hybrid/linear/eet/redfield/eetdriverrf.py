import numpy as np

from pyrho import ham, redfield, spec

def main(tau_c, T, lamda):
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

#start in [1,1] for populations
    rho_g = np.zeros((nsite,nsite))
#   rho_g[0,0] = 1.0
    rho_g[1,1] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1.],
                       [ 1.,  0.,  0.],
                       [ 1.,  0.,  0.]])

        
    for omega_c in [1/tau_c]:
        for beta in [1./kT]:
            for lamda in [lamda]:
                for method in ['Redfield','TCL2']:

                    t_final = 2000.
                    dt = 1.
                    lamda = lamda
                    kT = 1./beta
                    spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, hbar=hbar)
                    
                    
                    my_redfield = redfield.Redfield(my_ham, method = method)

    #               my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split, use_PD=False)
                    times, rhos_site,rhos_eig = my_redfield.propagate(rho_g, 0.0, t_final, dt)

     #               my_spec = spec.Spectroscopy(dipole, my_redfield)
    #              omegas, intensities = my_spec.absorption(-1500., 1600., 0.02, rho_g, t_final, dt, dipole_file =
    #                       'dipole_eet_%s_tauc%0.01f_T%0.01f_lamda%0.01f.dat'%(method,tau_c,T,lamda), is_damped=True)

                    with open('pop_eet_%s_tauc%0.01f_T%0.01f_lamda%0.01f.dat'%(method,tau_c,T,lamda), 'w') as f:
                         for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                          f.write('%0.8f %0.8f %0.8f\n'%(time, rho_site[1,1].real, rho_site[2,1].real))


    #              with open('eet_test_%s_tauc%0.01f_T%0.01f_lamda%0.01f.dat'%(method,tau_c,T,lamda), 'w') as f:
    #                   for (omega, intensity) in zip(omegas, intensities):
    #                       f.write('%0.8f %0.8f\n'%(omega-100, intensity))

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) != 3:
        print 'usage: run'
        sys.exit(1)
    tau_c = float(args[0])
    T = float(args[1])
    lamda = float(args[2])
    main(tau_c, T, lamda)
