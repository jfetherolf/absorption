import numpy as np

from pyrho import ham, redfield, spec

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
    dipole = np.array([[ 0.,  0.,  0.],
                       [ 0.,  0.,  0.5],
                       [ 0.,  0.5,  0.]])

    for omega_c in [0.3]:
        for beta in [1.]:
            for t_final in [50]:
                for dt in [0.005]:
                    lamda = 0.25
                    kT = 1./beta
                    spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath
                    t_init = 0.0
                    
                    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)

                    my_redfield = redfield.Redfield(my_ham, method='Redfield', is_secular=True)
#                   times, rhos_site, rhos_eig = my_redfield.propagate(rho_g, t_init, t_final, dt)

                    my_spec = spec.Spectroscopy(dipole, my_redfield)
                    omegas, intensities = my_spec.absorption(-4.+eps, 4.+eps, 0.02, rho_g, t_init, t_final, dt)

                    with open('2ndexcitation.dat', 'w') as f:
                        for (omega, intensity) in zip(omegas, intensities):
                            f.write('%0.8f %0.8f\n'%(omega-eps, intensity))

if __name__ == '__main__':
    main()
