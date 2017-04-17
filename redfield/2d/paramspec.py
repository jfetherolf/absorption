""" Example usage of pyrho to generate 2D spectra, specifically
    Fig. 2 in Chen et al., J. Chem. Phys. 132, 024505 (2010)
"""

import numpy as np

def main():

    hbar = 1.   # in cm-1 * fs

    ham_sys = np.array([[ 0., -1.],
                          [ -1.,  0.]])
    
    lamda = 0.5

    omega_r = (2/hbar)*np.sqrt(( ham_sys[0,0]-ham_sys[1,1])**2 / 4.0 + ham_sys[0,1]**2 )

    print 'The Rabi frequency of the system is',omega_r,'fs^-1'

    for omega_c in [0.1,0.3,1.0]:
        for beta in [1.0,3.0]:
            eta = max((2*lamda)/(beta*(hbar*omega_c)**2),(2*lamda)/(np.pi*hbar*omega_c))
            print 'When beta =',beta,'and omega_c =',omega_c,'dimensionless applicability parameter eta is',eta

if __name__ == '__main__':
    main()
