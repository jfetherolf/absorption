""" Example usage of pyrho to generate 2D spectra, specifically
    Fig. 2 in Chen et al., J. Chem. Phys. 132, 024505 (2010)
"""

import numpy as np
from pyrho import ham, redfield, frozen, hybrid, spec

def main():
    nbath = 2

    kB = 0.69352    # in cm-1 / K
    hbar = 5308.8   # in cm-1 * fs

    # System Hamiltonian
    # n = 0 is ground state

    # One-exciton Hamiltonian
    ham_sys_x = np.array([[ -50., -100.],
                          [ -100.,  50.]])
    # One-exciton sys-bath coupling
    nx = ham_sys_x.shape[0]
    ham_sysbath_x = []
    
    for b in range(nbath):
        ham_sysbath_b = np.zeros((nx,nx))
        for m in range(nx):
            ham_sysbath_b[m,m] = (m==b)
        ham_sysbath_x.append(ham_sysbath_b)
    # One-exciton dipole moments
    dipole_x = np.array([ 1., -0.2])

    # Important: expand the Hilbert space (convert to biexciton space)
    ham_sys, ham_sysbath, dipole = spec.convert_to_xx(ham_sys_x, ham_sysbath_x, dipole_x)
    nsite = ham_sys.shape[0]
    
    T = 77.
    lamda = 60.
    tau_c = 100. # in fs
    omega_c = 1./tau_c
    kT = kB*T

        
    spec_density_1 = [['ohmic-lorentz', lamda, omega_c]]*nbath
    spec_density_2 = [['ohmic-lorentz', lamda, omega_c]]*nbath


    my_ham = ham.Hamiltonian(ham_sys, ham_sysbath, spec_density_1, kT)
    my_ham_slow = ham.Hamiltonian(ham_sys, ham_sysbath, spec_density_1, kT, sample_wigner=False)
    my_ham_fast = ham.Hamiltonian(ham_sys, ham_sysbath, spec_density_2, kT)


    # Numerical propagation parameters
    t_final, dt = 500., 0.1

    # Waiting time parameters
    T_init, T_final, dT = 0., 700., 100.

    rho_g = np.zeros((nsite,nsite))
    rho_g[0,0] = 1.0

    omega_split = np.zeros((nbath))

    for n in range(1,nbath):
        omega_split[n] = 0.5

    for lpath in ['total']:
        nmode = 300
        ntraj = int(1E1)
        my_frozen = frozen.FrozenModes(my_ham_slow, nmode=nmode, ntraj=ntraj,)
        my_redfield = redfield.Redfield(my_ham_fast, method='Redfield')

        my_hybrid = hybrid.Hybrid(my_ham, my_frozen, my_redfield, omega_split = omega_split, use_PD=False)

        my_spec = spec.Spectroscopy(dipole, my_hybrid)

        omegas, intensities = my_spec.absorption(
                    -400., 400., 2., 
                    rho_g, t_final, dt)

        with open('abs_%s_FrozenRF_dt-%0.0f_tf-%0.0f.dat'%(lpath,dt,t_final), 'w') as f:
            for (omega, intensity) in zip(omegas, intensities):
                f.write('%0.8f %0.8f\n'%(omega, intensity))

        omega1s, omega3s, t2s, spectra = my_spec.two_dimensional(
                    -400., 400., 10.,
                    -400., 400., 10.,
                    T_init, T_final, dT,
                    rho_g, t_final, dt, lioupath=lpath)

        for t2, spectrum in zip(t2s, spectra):
            with open('2d_%s_t2-%0.1f_Frozen_dt-%0.0f_tf-%0.0f.dat'%(lpath,t2,method,dt,t_final), 'w') as f:
                for w1 in range(len(omega1s)):
                    for w3 in range(len(omega3s)):
                        f.write('%0.8f %0.8f %0.8f\n'%(omega1s[w1], omega3s[w3], spectrum[w3,w1]))
                    f.write('\n')
if __name__ == '__main__':
    main()
