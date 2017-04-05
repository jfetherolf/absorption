import sys
import numpy as np

from pyrho import ham, redfield

def main():
    nsite = 2
    nbath = 1
    hbar = 1.
    eps = 1.

    # System Hamiltonian
    ham_sys = np.array([[eps,   1.0],
                        [1.0,  -eps]])

    # System part of the the system-bath interaction
    # - a list of length 'nbath'
    # - currently assumes that each term has uncorrelated bath operators
    ham_sysbath = []
    ham_sysbath.append(np.array([[1.0,  0.0], 
                                 [0.0, -1.0]]))

    # Initial reduced density matrix of the system
    rho_0 = np.array([[1.0, 0.0],
                      [0.0, 0.0]])

    for lamda in [0.25]: 
        for omega_c in [0.25]:
            
            t_final = 50.
            dt = 0.01
            beta = 0.5
            kT = 1./beta        
            
            # Spectral densities - a list of length 'nbath'
            spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

            my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
            
            my_redfield = redfield.Redfield(my_ham, method='TCL2', is_secular=False)
            
            times, rhos_site, rhos_eig = my_redfield.propagate(rho_0, 0.0, t_final, dt)
                

            with open('pop_tanh_2015_omegac-%0.1f_lam-%0.2f_beta-%0.1f.dat'%(omega_c,lamda,beta), 'w') as f:
                for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                    f.write('%0.8f %0.8f\n'%(time, rho_site[0,0].real - rho_site[1,1].real))

if __name__ == '__main__':
    main()
