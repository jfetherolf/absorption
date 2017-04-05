import numpy as np

from pyrho import ham, redfield, spec, hybrid, frozen

def main(omega_c, beta,split,run):
    nsite = 1+2
    nbath = 2#+1
    
    eps = 0.

    # System Hamiltonian
    # n = 0 is ground state
    for V in [1.]:
        ham_sys = np.array([[ 0.,  0.,  0.],
                            [ 0., eps, -V],
                            [ 0., -V, -eps]])

        # System part of the the system-bath interaction
        ham_sysbath = []
   #     ham_sysbath.append(np.array([[ 0.,  0.,  0.],
    #                        [ 0., 0., 1.],
     #                       [ 0., 1., 0.]]))

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

            
        for omega_c in [omega_c]:
            for beta in [beta]:
                for nmode in [300]:

                    omega_r = 2*np.sqrt( (ham_sys[1,1]-ham_sys[2,2])**2 / 4.0 + ham_sys[1,2]**2 )

                    omega_split = []

                    for n in range(nbath):
                       omega_split.append(omega_r/split)
        #                  omega_split.append(split)
        #                  omega_split.append(1e-10)


                    ntraj = int(1e2)
                    t_final = 20.
                    dt = 0.02
                    lamda = 100.
                    kT = 1./beta
                    spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                    my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, sample_wigner=False)
                    my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                    my_frozen = frozen.FrozenModes(my_ham_slow, nmode=nmode, ntraj=ntraj)
                    my_redfield = redfield.Redfield(my_ham_fast, method='TCL2')

                    my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split, use_PD=False)

        #               time, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)

                    my_spec = spec.Spectroscopy(dipole, my_hybrid)
                    omegas, intensities = my_spec.absorption(-60.+eps, 60.+eps, 0.5, rho_g, t_final, dt, dipole_file = 'dipole_hybrid_omegac%0.1f_beta%0.1f_run%d.dat'%(omega_c,beta,run), is_damped=True)

                #   with open('abs_hybrid_redfield_fm_omegac%0.1f_beta%0.1f_split%0.1f_run%d.dat'%(omega_c,beta,omega_split[1],run), 'w') as f:
                    with open('abs_hybrid_diag_omegac%0.1f_beta%0.1f_lambda%0.1f_split%0.1f_run%d.dat'%(omega_c,beta,lamda,omega_split[1],run), 'w') as f:
                        for (omega, intensity) in zip(omegas, intensities):
                            f.write('%0.8f %0.8f\n'%(omega-eps, intensity))


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) != 4:
        print 'usage: run'
        sys.exit(1)
    omega_c = float(args[0])
    beta = float(args[1])
    split = float(args[2])
    run = float(args[3])
    main(omega_c, beta,split,run)
