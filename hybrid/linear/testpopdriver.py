import numpy as np

from pyrho import ham, frozen, redfield, hybrid

def main():
    nsite = 2
    nbath = 2

    eps = 0.

    # System Hamiltonian
    # n = 0 is ground state
    ham_sys = np.array([[ eps, -1.],
                        [ -1., eps]])

    # System part of the the system-bath interaction
    ham_sysbath = np.array([[ 1., 0.],
                            [ 0., 1.]])

    rho_0 = np.array([[ 1., 0.],
                      [ 0., 0.]])

    split = []
    for n in range(nbath):
        split.append(float(1e16))


    for lamda in [0.5]: 
            for beta in [1.]:
                omega_c = 0.3
                kT = 1/beta
                # Spectral densities - a list of length 'nbath'
                spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

                #TODO(TCB): Make this cleaner. Write a Hamiltonian.copy() method?
                my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
                my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)

                ntraj = int(1e2)
                my_frozen = frozen.FrozenModes(my_ham_slow, nmode=300, ntraj=ntraj)
                times, rhos_site, rhos_eig = my_frozen.propagate(rho_0, 0.0, 50.0, 0.1)
                my_redfield = redfield.Redfield(my_ham_fast, method='Redfield')

                my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split=split)
                times, rhos_site, rhos_eig = my_hybrid.propagate(rho_0, 0.0, 50.0, 0.1)

                with open('test_pop_site_beta-%0.1f_lam-%0.2f_ntraj-%d.dat'%(beta,lamda,ntraj), 'w') as f:
                    for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                        f.write('%0.8f %0.8f %0.8f\n'%(time, rho_site[0,0].real, 
                                                             rho_site[1,1].real))


if __name__ == '__main__':
    main()
