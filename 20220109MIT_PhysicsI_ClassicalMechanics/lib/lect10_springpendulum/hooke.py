
import math
from typing import Tuple
from collections import namedtuple

Sap = namedtuple('Sap', ['sin', 'cos', 'tan'])

class Spring:
    def __init__(self, k:float, m:float) -> None:
        self._k = k
        self._m = m

    def force(self, x:float)->float:
        '''Hooke's Law

        F is independent to mass of the object;
        '''
        return self._k * x

    @property
    def oscillation_period(self)->float:
        '''
        T ∝ m * k;

        T is independent to x as long as Hooke's law holds;
        '''
        return 2 * math.pi * math.sqrt(self._m / self._k)

    @property
    def oscillation_frequency(self)->float:
        return 1 / self.oscillation_period

    def differential_equation(self)->str:
        '''
        ma = -kx

        mẍ + kx = 0
        '''
        return 'ẍ + k/m * x = 0'

    def x_over_time(self)->str:
        '''

        A: amplitude. The amplitude of a periodic variable is a measure of its change in a single period (such as time or spatial period).

        ω: angular frequency; unit: rad / sec;

        φ: phase angle;

        T = 2π / ω; unit: sec

        f = 1 / T; unit: Hz

        1st derivative: ẋ = - A ω sin(ωt + φ)

        2nd derivative: ẍ = - A ω^2 cos(ωt + φ) = - ω^2 x;

        substitute into the "differential_equation"

        - ω^2 x + k/m * x = 0

        ω^2 = k/m
        '''
        return 'x = A * cos(ωt + φ)'

    @property
    def angular_frequency(self)->float:
        return math.sqrt(self._k / self._m)

class Pendulum:
    G:float = +9.8

    def __init__(self, m:float, l:float) -> None:
        """init a pendulum object with massive bob, massless rod, amplitude

        Args:
            m (float): mass of bob, unit: kg

            l (float): length of rod, unit: m
        """
        self._m = m
        self._l = l

    @classmethod
    def sap(cls, theta:float)->Tuple:
        '''Small Angle Proximation

        where θ << 1;

        sin(θ) = 0

        cos(θ) = 1 - θ^2 / 2 = 1

        tan(θ) = θ
        '''
        return Sap(0, 1, theta)

    @property
    def sho(self)->str:
        '''Simple Harmonic Oscillation

        such a beautiful result makes me cry :P
        '''
        return 'ẍ + (g / l) * x = 0'

    @property
    def angular_frequency(self)->float:
        return math.sqrt(self.G / self._l)

    @property
    def oscillation_period(self)->float:
        '''Physic works @WL
        '''
        return 2 * math.pi / self.angular_frequency

def client_code()->None:
    h = Spring(10, 0.1)
    print(h.angular_frequency)
    print(h.oscillation_period)
    print(h.oscillation_frequency)


    print(Pendulum.sap(1).sin)
    p1 = Pendulum(15, 5.18)
    print(p1.oscillation_period)

if __name__ == '__main__':
    client_code()
