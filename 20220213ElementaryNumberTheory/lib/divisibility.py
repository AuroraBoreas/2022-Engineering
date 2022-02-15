import dataclasses
import math

@dataclasses.dataclass
class Divisibility:
    @property
    def division_algorithm(a:int, b:int)->str:
        return f'{a} = q*{b} + r, where 0 <= r < |b|;'

    def gcd(self, a:int, b:int)->int:
        '''
        euclidean algorithm

        complexity : Q(5), P39

        gcd(a, b) == gcd(b, r), where r is remainder of a / b;

        '''
        return a if b == 0 else self.gcd(b, a % b)

    def lcm(self, a:int, b:int)->float:
        '''
        lcm(a, b) denotes the least common multiple of two nonzero integers a, b
        
        is the positive interger m satisfying the following:
        
        (a) a | m and b | m;

        (b) if a | c and b | c, with c > 0, then m <= c;

        lcm(a, b) <= |ab|

        gcd(a, b) * lcm(a, b) = ab
        '''
        return a * b / self.gcd(a, b)

if __name__ == '__main__':
    d = Divisibility()
    print(math.gcd(111, 12))
    print(d.lcm(111, 12))