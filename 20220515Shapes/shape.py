from abc import abstractmethod
import math

class C3DShape:
    '''
    Common 3D Shape @ZL, 20220516
    '''
    @abstractmethod
    def get_surface_area(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_volume(self) -> float:
        raise NotImplementedError()

class Sphere(C3DShape):
    def __init__(self, r:float) -> None:
        self._r = r

    def get_surface_area(self) -> float:
        return 4 * math.pi * math.pow(self._r, 2)

    def get_volume(self) -> float:
        return 4 * math.pi * math.pow(self._r, 3) / 3

class Torus(C3DShape):
    def __init__(self, r:float, R:float) -> None:
        self._r = r
        self._R = R

    def get_surface_area(self) -> float:
        return (2 * math.pi * self._R) * (2 * math.pi * self._r)

    def get_volume(self) -> float:
        return (2 * math.pi * self._R) * (math.pi * math.pow(self._r, 2))

class Cylinder(C3DShape):
    def __init__(self, r:float, h:float) -> None:
        self._r = r
        self._h = h

    def get_surface_area(self) -> float:
        return 2 * math.pi * self._r * (self._r + self._h)

    def get_volume(self) -> float:
        '''cooking a pizza -> pi x z x z x a'''
        return math.pi * math.pow(self._r, 2) * self._h

class Cone(C3DShape):
    def __init__(self, r:float, h:float) -> None:
        self._r = r
        self._h = h

    def get_surface_area(self) -> float:
        return math.pi * self._r * (self._r + math.hypot(self._r, self._h))

    def get_volume(self) -> float:
        return math.pi * self._r * self._r * self._h / 3

class Cube(C3DShape):
    def __init__(self, edge:float) -> None:
        self._edge = edge

    def get_surface_area(self) -> float:
        return math.pow(self._edge, 2) * 6

    def get_volume(self) -> float:
        return math.pow(self._edge, 3)

class Cuboid(C3DShape):
    def __init__(self, l:float, w:float, h:float) -> None:
        self._l = l
        self._w = w
        self._h = h

    def get_surface_area(self) -> float:
        return 2 * (self._l * self._w + self._l * self._h + self._w * self._h)

    def get_volume(self) -> float:
        return self._l * self._w * self._h

class TriangularPyramid(C3DShape):
    def __init__(self, base_area:float, perimeter:float, slant_length:float) -> None:
        self._base_area    = base_area
        self._perimeter    = perimeter
        self._slant_length = slant_length

    def get_surface_area(self) -> float:
        return self._base_area + self._perimeter * self._slant_length / 2

    def get_volume(self, height:float) -> float:
        return self._base_area * height / 3

class SquarePyramid(TriangularPyramid):
    def __init__(self, base_area:float, perimeter:float, slant_length:float) -> None:
        super().__init__(base_area, perimeter, slant_length)

    def get_surface_area(self) -> float:
        return super().get_surface_area()

    def get_volume(self, height:float) -> float:
        return super().get_volume(height)

class Prism(C3DShape):
    def __init__(self, base_area: float, base_perimeter: float, length: float) -> None:
        '''
        Triangle Prism
        '''
        self._base_area = base_area
        self._base_perimeter = base_perimeter
        self._length = length

    def get_surface_area(self) -> float:
        return 2 * self._base_area + self._base_perimeter * self._length

    def get_volume(self) -> float:
        return self._base_area * self._length

class C2DShape:
    '''
    Common 2D Shape @ZL, 20220516
    '''
    @abstractmethod
    def get_perimeter(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_internal_angles(self, n:int) -> int:
        return (n - 2) * 180

    @abstractmethod
    def get_diagonals(self, n:int) -> int:
        return n * (n - 3) / 2

class Triangle(C2DShape):
    def __init__(self, a:float, b:float, c:float) -> None:
        self._a = a
        self._b = b
        self._c = c

    def get_area(self) -> float:
        '''general -> Heron's Formula:

        step1: find perimeter / 2;

        step2: find area;
        '''
        s:float = self.get_perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def get_internal_angles(self, n: int) -> int:
        return super().get_internal_angles(n)

    def get_perimeter(self) -> float:
        return self._a + self._b + self._c

    def get_diagonals(self, n: int) -> int:
        return super().get_diagonals(n)

    @property
    def sine_law(self, A:float, B:float, C:float) -> bool:
        return self._a / math.sin(A) == self._b / math.sin(B) == self._c / math.sin(C)

    @property
    def consine_law(self, C:float) -> bool:
        return self._c == self._a * self._a + self._b * self._b - 2 * self._a * self._b * math.cos(C)

    @property
    def tangent_law(self, A:float, B:float) -> bool:
        return (self._a - self.b) / (self._a + self._b) == math.tan((A - B) / 2) / math.tan((A + B) / 2)

class Polygon(C2DShape):
    def __init__(self) -> None:
        super().__init__()

    def get_diagonals(self, n: int) -> int:
        return super().get_diagonals(n)

    def get_internal_angles(self, n: int) -> int:
        return super().get_internal_angles(n)

class Circle(C2DShape):
    def __init__(self, r:float) -> None:
        self._r = r

    def get_area(self) -> float:
        return math.pi * self._r * self._r

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._r

class Ellipse(C2DShape):
    def __init__(self, a:float, b:float) -> None:
        '''
        a : semi-major axis

        b : semi-minor axis
        '''
        self._a = a
        self._b = b

    def get_area(self) -> float:
        return math.pi * self._a * self._b

    def get_perimeter(self) -> float:
        '''approximate reulst, squiggly'''
        return 2 * math.pi * math.sqrt((self._a * self._a + self._b * self._b) / 2)

    @property
    def eccentricity(self) -> float:
        return math.sqrt(self._a * self._a - self._b * self._b) / self._a
