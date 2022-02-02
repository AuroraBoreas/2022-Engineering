
import math
from typing import NewType
Angle = NewType('Angle', float)

class Triangle:
    def __init__(self, base:float, height:float) -> None:
        self._base   = base
        self._height = height

    def area(self)->float:
        return .5 * self._base * self._height

    @staticmethod
    def cosine_rule(a:float, b:float, C:Angle)->float:
        return math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))

    @staticmethod
    def heron_formula(a:float, b:float, c:float)->float:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @staticmethod
    def sine_rule(a:float, b:float, c:float, A:Angle, B:Angle, C:Angle)->bool:
        return a / math.sin(A) == b / math.sin(B) == c / math.sin(C)

class Trigonometry:
    _rule:str = 'SOH - CAH - TOA'
    _hyp:str  = 'H'
    _opp:str  = 'O'
    _adj:str  = 'A'

    @property
    def sin(self)->str:
        return f"sinθ = {self._opp} / {self._hyp}"

    @property
    def cos(self)->str:
        return f"cosθ = {self._opp} / {self._hyp}"

    @property
    def tan(self)->str:
        return f"tanθ = {self._opp} / {self._adj}"

    @property
    def csc(self)->str:
        return f"cscθ = {self._hyp} / {self._opp}"

    @property
    def sec(self)->str:
        return f"secθ = {self._hyp} / {self._opp}"

    @property
    def cot(self)->str:
        return f"cotθ = {self._adj} / {self._opp}"

    @property
    def arcsin(self)->str:
        '''
        invert
        '''
        return f"arcsinθ = sin ^ -1 (θ)"

def sum_of_square(n:int)->int:
    return n * (n + 1) * (2 * n + 1) / 6
