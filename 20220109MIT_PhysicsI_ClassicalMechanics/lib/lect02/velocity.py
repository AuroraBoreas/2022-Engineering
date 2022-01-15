"""


this module is to calculate velocity.

## Why
MIT, classic mechanics I, lect02

## Author
@ZL, 20220111

## Changelog
- v0.01, initial build

"""

from dataclasses import dataclass

@dataclass
class Velocity:
    """ unit: m/s """
    def __init__(self, x1:float, x2:float, t1:float, t2:float) -> None:
        self._x1 = x1
        self._x2 = x2
        self._t1 = t1
        self._t2 = t2

    @property
    def v_bar(self)->float:
        """ velocity is sign sensitive; speed is sign insensitive """
        return (self._x1 - self._x2) / (self._t1 - self._t2)

    @property
    def v_ins(self)->str:
        return 'dx / dt'

@dataclass
class Acceleration:
    """ unit: m/s^2 """
    def __init__(self, v1:float, v2:float, t1:float, t2:float) -> None:
        self._v1 = v1
        self._v2 = v2
        self._t1 = t1
        self._t2 = t2

    @property
    def a_bar(self)->float:
        """ try to image what happening! not just curve """
        return (self._v2 - self._v1) / (self._t2 - self._t1)


