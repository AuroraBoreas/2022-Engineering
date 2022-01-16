"""
uniform circular motion


"""

import math

class UCM:
    def __init__(self, r:float, t:float) -> None:
        self._r = r
        self._t = t

    @property
    def T(self)->float:
        ''' sec per circle
        '''
        return self._t

    @property
    def F(self)->float:
        '''Hz
        '''
        return 1 / self._t

    @property
    def av(self)->float:
        ''' radius per sec

        ω (angular_velocity) = 2π / T = 2πf
        '''
        return (2 * math.pi) / self._t

    @property
    def speed(self)->float:
        '''
        v = 2πr / T = ωr
        '''
        return self.av * self._r

    @property
    def ac(self)->float:
        ''' magnitude

        direction is always pointing to circle center;

        centripetal_accel.(or ac) = v**2 / r = ω**2 * r
        '''
        return self.av**2 * self._r

    @property
    def centrifuge(self)->str:
        return 'centrifuge'

def client_code()->None:
    u = UCM(0.1, 0.1)
    print(u.av, u.speed, u.ac)

    u1 = UCM(0.15, 1/60)
    print(u1.ac)

if __name__ == '__main__':
    client_code()
