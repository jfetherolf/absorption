import sys
import numpy as np

from pyrho import ham, frozen, redfield, hybrid

def main():
    nsite = 2
    nbath = 1
    hbar = 1.
    eps = 0.

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
           
            omega_r = 2*np.sqrt( (ham_sys[0,0]-ham_sys[1,1])**2/4.0 + ham_sys[0,1]**2 )/hbar
            omega_split = []
            for n in range(nbath):
#               omega_split.append(max(omega_r/4., omega_c))
                omega_split.append(0.)
            nmode = 300
            ntraj = int(1e0)
            t_final = 25.
            dt = 0.01
            beta = 5.0
            kT = 1./beta        
            
            # Spectral densities - a list of length 'nbath'
            spec_densities = [['ohmic-lorentz', lamda, omega_c]]*nbath

            my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)
            my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT, sample_wigner=True)
            my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_densities, kT)

            my_frozen = frozen.FrozenModes(my_ham_slow, nmode=nmode, ntraj=ntraj)

            my_redfield = redfield.Redfield(my_ham, method='TCL2', is_secular=False)
            
            my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split, use_PD=False)

            times, rhos_site, rhos_eig = my_hybrid.propagate(rho_0, 0.0, t_final, dt)
                

 #           with open('poptest_hybridtcl2_PD_2015_omegac-%0.1f_lam-%0.1f_beta-%0.1f.dat'%(omega_c,lamda,beta), 'w') as f:
            with open('bleh', 'w') as f:
                for (time, rho_site, rho_eig) in zip(times, rhos_site, rhos_eig):
                    f.write('%0.8f %0.8f\n'%(time, rho_site[0,0].real - rho_site[1,1].real))

if __name__ == '__main__':
    main()
