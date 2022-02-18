
from numpy import math


class Diophantine:
    "丢番图不定方程"
    @property
    def linear_diophantine_equation()->str:
        return 'ax + by = c, where a, b, c ∈ Integer, and a, b are not both zero;'

    def hassolution(a:int, b:int, c:int)->bool:
        '''
        p45/451
        
        '''
        d = math.gcd(a, b)
        return c % d == 0

if __name__ == '__main__':
    d = Diophantine.hassolution(172, 20, 1000)
    d = Diophantine.hassolution(5, 22, 18)
    print(d)