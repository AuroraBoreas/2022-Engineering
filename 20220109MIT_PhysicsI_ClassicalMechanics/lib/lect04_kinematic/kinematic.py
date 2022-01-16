
from dataclasses import dataclass
import math

@dataclass
class FreeFalling:
    G:float = +9.8 # m/sec**2

    def __init__(self, x0:float, v0:float, theta:float) -> None:
        self._x0    = x0
        self._v0    = v0
        self._theta = theta

    @property
    def max_hight(self)->float:
        return (self._v0 * math.sin(self._theta))**2 / (2 * self.G)

    @property
    def when_max_hight(self)->float:
        return (2 * self._v0 * math.sin(self._theta)) / self.G

    @property
    def os(self)->float:
        return (self._v0**2 * math.sin(2 * self._theta)) / self.G - self._x0

    def time(self, h:float)->float:
        '''
        h = 1/2 * g * t**2;
        '''
        return math.sqrt((2 * h) / self.G)

    def velocity(self, t:float)->float:
        return self.G * t
