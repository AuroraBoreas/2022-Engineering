from __future__ import annotations
from dataclasses import dataclass
import math
from collections import namedtuple
from typing import Tuple

gmf = namedtuple('gmf', ['x', 'y', 'z'])

@dataclass
class Vector:
    def __init__(self, x:float, y:float, z:float) -> None:
        self._x = x
        self._y = y
        self._z = z
        self._xyz = (x, y, z)

    def __str__(self) -> str:
        return 'Vector: ({0}x̂, {1}ŷ, {2}ẑ)'.format(*self._xyz)

    def magnitude(self)->float:
        return math.sqrt(sum([i**2 for i in self._xyz]))

    def dot_product_01(self, other:Vector)->Vector:
        return Vector(*(x * y for x, y in zip(self._xyz, other._xyz)))

    def dot_product_02(self, other:Vector, theta:float)->float:
        return self.magnitude() * other.magnitude() * math.cos(theta)

    def cross_product_01(self, other:Vector)->Vector:
        '''recipe 1
        1) duplicate vector "A over B" 3 times, with unit(x̂, ŷ, ẑ) at middle;
        2) cross over

        '''
        return Vector(
            self._y * other._z - self._z * other._y,
            self._z * other._x - self._x * other._z,
            self._x * other._y - self._y * other._x
        )

    def cross_product_02(self, other:Vector, theta:float)->float:
        '''corkscrew rule (potato):
        1) always, always work with "right-handed coordinate system", by definition: make you a diagram for which x cross y is z;
        2) or I will kill you!

        A x B == -B x A
        '''
        return self.magnitude() * other.magnitude() * math.sin(theta)

    def one_dimension_motion(self)->str:
        ''' substitute x -> y -> z
        then we have 2D or 3D motion
        '''
        return 'Xt = Xo + Vox * t + 0.5 * Ax * t^2'

    def general_motion_form_3D(self)->Tuple:
        ''' decompose
        '''
        return (
            Vector('Xt', 'Yt', 'Zt').__str__(),
            Vector('ẋ', 'ẏ', 'ż').__str__(),
            Vector('ẍ', 'ÿ', 'z̈').__str__(),
        )

if __name__ == '__main__':
    v1 = Vector(3, -5, 6)
    v2 = Vector(0, 2, 0)
    print(v1)
    print(v2)
    print(v1.dot_product_01(v2))
    print(v1.magnitude())
    print(v1.cross_product_01(v2))
    print(v2.general_motion_form_3D())
