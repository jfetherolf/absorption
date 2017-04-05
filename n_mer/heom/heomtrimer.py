import numpy as np

from pyrho import ham, heom, spec

def main(omega_c,beta,K,L):
    
    nsite = 1+3
    nbath = 3

    eps = 1.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ 0.,  0.,  0.,  0.],
                        [ 0., eps, -2.,  0.],
                        [ 0., -2., 2*eps, -1.],
                        [ 0., 0., -1.,  4*eps]])

    # System part of the the system-bath interaction
    ham_sysbath = []
    for n in range(1,nsite):
        ham_sysbath_n = np.zeros((nsite,nsite))
        ham_sysbath_n[n,n] = 1.0
        ham_sysbath.append( ham_sysbath_n )

    rho_g = np.zeros((nsite,nsite))
    rho_g[0,0] = 1.0

    # Dipole operator connecting the ground state to the excited states
    dipole = np.array([[ 0.,  1.,  1., 1.],
                       [ 1.,  0.,  0., 0.],
                       [ 1.,  0.,  0., 0.],
                       [ 1.,  0.,  0., 0.]])

 

    for lamda in [0.5]:
        for omega_c in [omega_c]:
            for beta in [beta]:
                for L in [L]:
                    for K in [K]:
                        kT = 1./beta
                        spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath
        
                        t_init = 0.0 
                        t_final = 30.0
                        dt = 0.02

                        my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)

                        my_heom = heom.HEOM(my_ham, L=L, K=K)
#                       times, rhos_site, rhos_eig = my_heom.propagate(rho_g, t_init, t_final, dt)
   
                        my_spec = spec.Spectroscopy(dipole, my_heom)
                        omegas, intensities = my_spec.absorption(-5.+eps, 7.+eps, 0.05, rho_g, t_final, dt, dipole_file = 'dipole_heomtrimer_omegac%0.1f_beta%0.1f.dat'%(omega_c,beta), is_damped=True)


                        with open('heomtrimer_L%0.1f_K%0.1f_omegac%0.1f_beta%0.1f_lamda%0.1f.dat'%(L,K,omega_c,beta,lamda), 'w') as f:
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
    L = int(args[2])
    K = int(args[3])
    main(omega_c,beta,K,L)
