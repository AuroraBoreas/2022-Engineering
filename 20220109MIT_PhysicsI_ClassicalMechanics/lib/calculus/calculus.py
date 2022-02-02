"""
this module summarizes calculus

## Author
@ZL, 20220202

## Changelog
- v0.01, initial build

"""

from __future__ import annotations
import math

def pow(x:float, a:float)->float:
    return x ** a

def exp(a:float, x:float)->float:
    return a ** x

def reciprocal(x:float)->float:
    return 1 / x

class Power:
    def __init__(self, base:float, p:float) -> None:
        self._base = base
        self._p    = p

    def __str__(self) -> str:
        return f'{self._base} ^ {self._p}'

    def __call__(self)->float:
        return self._base ** self._p

    def __mul__(self, other:Power)->Power:
        return Power(self._base, self._p + other._p)

    def __div__(self, other:Power)->Power:
        return self._base ** (self._p - other._p)

    def reciprocal(self)->Power:
        return Power(self._base, self._p * -1)

    def pow(self, n:float)->Power:
        return Power(self._base, self._p * n)

class Logarithm:
    def __init__(self, base:int, x:float) -> None:
        self._base = base
        self._x    = x

    def __str__(self) -> str:
        return f'log{self._base} ({self._x})'

    def __call__(self)->float:
        return math.log(self._x, self._base)

    def __add__(self, other:Logarithm)->Logarithm:
        '''
        log(xy) = log(x) + log(y)
        '''
        return Logarithm(self._base, self._x * other._x)

    def __sub__(self, other:Logarithm)->Logarithm:
        '''
        log(x/y) = log(x) - log(y)
        '''
        return Logarithm(self._base, self._x / other._x)

    def reciprocal(self)->Logarithm:
        '''
        loga(b) = 1 / logb(a)
        '''
        return 1 / Logarithm(self._x, self._base)

    def change_base(self, k:int)->float:
        '''
        loga(b) = logk(b) / logk(a)
        '''
        return Logarithm(k, self._x)() / Logarithm(k, self._base)()

class Derivative:
    _natural:str = 'e ^ x'

    def __init__(self) -> None:
        self._f  = 'f(x)'
        self._g  = 'g(x)'
        self._fp = 'f\'(x)'
        self._gp = 'g\'(x)'

    def add(self)->str:
        '''
        limit law
        '''
        return f"[{self._f} + {self._g}]\' = {self._fp} + {self._gp}"

    def sub(self)->str:
        '''
        squeeze law
        '''
        return f"[{self._f} - {self._g}]\' = {self._fp} - {self._gp}"

    def mul(self)->str:
        return f"[{self._f} * {self._g}]\' = {self._fp} * {self._g} + {self._f} * {self._gp}"

    def div(self)->str:
        return f"[{self._f} / {self._g}]\' = ({self._fp} * {self._g} - {self._f} * {self._gp}) / ({self._g}) ^ 2"

    @property
    def chain(self)->str:
        '''
        high order function
        '''
        return f"[f • g(x)]\' = f\'(g(x)) * g\'(x)"

    @staticmethod
    def pow(x:int, a:float)->str:
        return f"[{x} ^ {a}]\' = {a} * {x} ^ {a-1}"

    def natural(self)->str:
        return f"[{self._natural}]\' = {self._natural}"

    @staticmethod
    def exp(a:int, x:float)->str:
        '''
        using natural as a model to prove this
        '''
        return f"[{a} ^ {x}]\' = ln{a} * ({a} ^ {x})"

    @staticmethod
    def log(b:int, x:float)->str:
        return f"[log{b}({x})]\' = 1 / (ln{b} * {x})"

    @staticmethod
    def sin(x)->str:
        '''
        sap: small angle approximation

        where 0 < θ << 1

        sinθ = θ

        cosθ = 1 - θ ^ 2 / 2 = 1

        tan = θ
        '''
        return f"sin\'({x}) = cos({x})"

    @staticmethod
    def cos(x)->str:
        return f"cos\'({x}) = -sin({x})"

    @staticmethod
    def tan(x)->str:
        return f"tan\'({x}) = sec^2({x})"

    @property
    def concave_up(self)->str:
        '''
        smile face + :), rotate 90 deg
        '''
        return f"f\'(x) > 0"

    @property
    def concave_down(self)->str:
        '''
        sad face - :(, rotate 90 deg
        '''
        return f"f\'(x) < 0"

    @property
    def implicit(self)->str:
        return 'i.e., x ^ 2 + y ^ 2 = 1'

    @property
    def inflection(self)->str:
        return 'decreasing <-> inflection_point <-> increasing'

    @property
    def mean_of_function(self)->str:
        return 'f average = [f(b) - f(a)] / (b - a)'

class Integral:
    def __init__(self) -> None:
        pass

    @property
    def substitute(self)->str:
        '''
        mechanism: chain rule of derivative
        '''
        return 'using Substitution to make integral computation easier, esp. pow, exp, log; x ^ x etc;'

    @staticmethod
    def antiderivative_power(x:int, a:int)->str:
        return f"∫{x}^{a} dx = x ^ {a + 1} / {a + 1} + C; where C is const"
