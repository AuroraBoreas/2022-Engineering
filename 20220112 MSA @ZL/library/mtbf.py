# https://www.ti.com/support-quality/reliability/temperature-change-FIT.html

from math import exp


def af(Ea:float, Tlow:float, Thigh:float)->float:
    '''
    AF - Acceleration factor

    Ea - Activation Energy, unit: eV

    k - Boltzmann Constant, 1.380649e-23, unit: K

    T - Temperature, unit: C

    '''
    k = 1.380649e-23
    return exp((Ea/k) * (1/Tlow - 1/Thigh))

if __name__ == '__main__':
    res = af(0.3, 55, 70)
    print(res)
