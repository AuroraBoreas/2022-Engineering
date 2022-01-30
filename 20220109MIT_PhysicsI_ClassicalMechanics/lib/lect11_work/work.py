
class Work:
    def __init__(self) -> None:
        pass

    def work(self, f:float, x:float)->float:
        '''one dimensional work: move an object from position A to position B with Force;

        W = Σ F * dx;

        unit: N*m = J;
        '''
        return f * x

    def kinetic_energy(self, m:float, v:float)->float:
        """Kinetic Energy: energy of motion

        F = ma = m * dv/dt;

        dx = v * dt;

        W = Σ m * dv * v = 1/2 * m * (υB^2 - υA^2);

        KE(Kinetic Energy) = 1/2 * m * v^2;
        """
        return 0.5 * m * v**2

    def work_energy_therom(self, KEa:float, KEb:float)->float:
        '''
        Wab = KEb - KEa

        it is independent to path
        '''
        return KEb - KEa

    def potential_energy(self)->str:
        '''Gravitational Potential Energy

        Gravitational potential energy is energy an object possesses

        because of its position in a gravitational field.

        The most common use of gravitational potential energy is for an object near the surface of the Earth

        where the gravitational acceleration can be assumed to be constant at about 9.8 m/s2

        mechanical energy is conserved only if the Force is conservative force like gravity;
        '''
        return 'mass * G * y'

    def is_roller_coaster_work(self, h:float, r:float)->bool:
        '''roller coaster

        it is not intuitive;

        h: original height of object

        r: radius of circle

        '''
        return h >= 5/2 * r

class Gravitational_Force:
    G:float = 6.67e-11
    T:int   = 24 * 60 * 60  # sec
    R:int   = 6_378 * 1_000 # meter
    M:float = 5.9722e24     # kg

    def __init__(self, m1:float, m2:float, r:float) -> None:
        self._m1 = m1
        self._m2 = m2
        self._r  = r

    def universal_law_of_gravity(self)->float:
        '''Newton's universal law of gravity

        G is constant coefficiency;
        '''
        return self._m1 * self._m2 * self.G / self._r**2

    def work(self)->float:
        '''
        Work from infinity to any position R before object 1 and object 2

        150 J is enough to kill a person;
        '''
        return -1 * self._m1 * self._m2 * self.G / self._r

def client_code()->None:

    pass

if __name__ == '__main__':
    client_code()
