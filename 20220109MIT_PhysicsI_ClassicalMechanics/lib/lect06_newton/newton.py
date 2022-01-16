"""
Newton's law

## environment
- gravity
- friction

"""

import sys
sys.path.append('.')

import math
from lib.utility.ttype import logging

class Earth:
    T:int   = 24 * 60 * 60  # sec
    R:int   = 6_378 * 1_000 # meter
    M:float = 5.9722e24     # kg

    def __init__(self) -> None:
        pass

    @property
    def av(self)->float:
        '''
        ω (angular_velocity) = 2π / T = 2πf
        '''
        return (2 * math.pi) / self.T

    @property
    def ac(self)->float:
        '''
        centripetal_accel.(or ac) = v**2 / r = ω**2 * r
        '''
        return self.av**2 * self.R

class NewtonsLaw:
    '''
    only available when speed of objects is less than light (3e8);
    '''

    def force(self, mass:float, acce:float)->float:
        '''1st Newton Law(magnitude): F = ma;

        unit of Force: kg * m / sec**2, or Newton
        '''
        return mass * acce

    @staticmethod
    def first_law()->str:
        '''
        Newton's first law, also called the "law of inertia",

        states that an object at rest remains at rest,

        and an object that is moving will continue to move straight and with constant velocity,

        if and only if there is no net force acting on that object;

        Newton's first law is valid only in an inertial reference frame
        '''
        return 'Fnet = 0 <=> dv/dt = 0'

    @staticmethod
    def second_law()->str:
        return 'Fnet = ma'

    @staticmethod
    def third_law()->str:
        '''
        The third law states that all forces between two objects exist in equal magnitude and opposite direction:

        if one object A exerts a force FA on a second object B,

        then B simultaneously exerts a force FB on A, and the two forces are equal in magnitude and opposite in direction:

        FA = -FB

        action = -reaction
        '''
        return 'Fa = -Fb'

def client_code()->None:
    e = Earth()
    logging.info(e.ac)
    n = NewtonsLaw()
    print(n.second_law())

if __name__ == '__main__':
    client_code()
    print(1e1)
