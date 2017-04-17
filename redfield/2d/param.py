""" Example usage of pyrho to generate 2D spectra, specifically
    Fig. 2 in Chen et al., J. Chem. Phys. 132, 024505 (2010)
"""

import numpy as np

def main():

    kB = 0.69352    # in cm-1 / K
    hbar = 5308.8   # in cm-1 * fs

    ham_sys = np.array([[ -50., -100.],
                          [ -100.,  50.]])
    
    lamda = 60.

    omega_r = (2/hbar)*np.sqrt(( ham_sys[0,0]-ham_sys[1,1])**2 / 4.0 + ham_sys[0,1]**2 )

    print 'The Rabi frequency of the system is',omega_r,'fs^-1'

    for omega_c in [0.10,0.0333,0.01]:
        for T in [77.,300.]:
            eta = max((2*lamda*kB*T)/((hbar*omega_c)**2),(2*lamda)/(np.pi*hbar*omega_c))
            print 'When T =',T,'and omega_c =',omega_c,'dimensionless applicability parameter eta is',eta

if __name__ == '__main__':
    main()
