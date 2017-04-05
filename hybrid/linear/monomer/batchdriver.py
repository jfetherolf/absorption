import numpy as np

from pyrho import ham, frozen, redfield, hybrid, spec

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
            for nmode in [300]:
                for method in ['Redfield','TCL2']:
                    
                    omega_split = []

                    for n in range(nbath):
    #                  omega_split.append(split)
                       omega_split.append(1e-10)


    #               t_init = 0.0
                    ntraj = int(1e0)
                    t_final = 30.
                    dt = 0.1
                    lamda = 0.1
                    kT = 1./beta
                    spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                    my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, sample_wigner=True)
                    my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)


                    my_frozen = frozen.FrozenModes(my_ham_slow, nmode=nmode, ntraj=ntraj)
                    my_redfield = redfield.Redfield(my_ham_fast, method=method)

                    my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split, use_PD=True)

    #               time, rhos_site,rhos_eig = my_hybrid.propagate(rho_g, 0.0, t_final, dt)
                  
                    my_spec = spec.Spectroscopy(dipole, my_hybrid)
                    omegas, intensities = my_spec.absorption(-4.+eps, 4.+eps, 0.02, rho_g, t_final, dt, dipole_file = 'dipole_hybrid_omegac%0.1f_beta%0.1f_%s.dat'%(omega_c,beta,method), is_damped=True)

                    with open('abs_hybrid_omegac%0.1f_beta%0.1f_lamda%0.1f_split%0.1f_%s.dat'%(omega_c,beta,lamda,omega_split[0],method), 'w') as f:
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
