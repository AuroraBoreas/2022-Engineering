"""
uniform circular motion


"""

import math

class UCM:
    def __init__(self, r:float, ) -> None:
        pass

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
    def omega(self)->float:
        ''' radius per sec
        ω (angular_velocity) = 2π / T
        '''
        return (2 * math.pi) / self._t

    @property
    def speed(self)->float:
        '''
        v = 2πr / T = ωr
        '''
        return self.omega * self._r

    @property
    def centripetal_acceleration(self)->float:
        ''' magnitude
        direction is always pointing to circle center;
        centripetal_accel. = v**2 / r = ω**2 * r
        '''
        return self.omega**2 * self._r
