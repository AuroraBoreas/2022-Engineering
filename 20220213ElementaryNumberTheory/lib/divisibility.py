
from typing import List
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

class Prime:
    @property
    def what()->str:
        '''
        prime vs composite
        '''
        return 'an integer p > 1 is called a prime, if its only positive divisors are 1 and p;'

    @staticmethod
    def is_prime(n:int)->bool:
        '''
        wilson's theorem

        note: 1 is not a prime by prime definition
        '''
        if n == 1: return False
        return math.factorial(n - 1) % n == n - 1

    @property
    def fta()->str:
        return '''
        every positive integer n > 1 is either a prime or a product of primes;
        this representation is unique, apart from the order in which the factors occur;

        canonical form:
        any positive integer n > 1

        n = p1^k1 * p2^k2 * ... * pr^kr
        '''

    @staticmethod
    def eratosthenes(n:int)->List:
        multiples = set()
        primes = []
        for i in range(2, n+1):
            if i not in multiples:
                primes.append(i)
                for j in range(i*i, n+1, i):
                    multiples.add(j)
        return primes

    def is_square(self, n:int)->bool:
        '''
        Python>=3.80, math.isquare(n)
        '''
        x = n // 2
        seen = set([x])
        while x * x != n:
            x = (x + (n // x)) // 2
            if x in seen: return False
            seen.add(x)
        return True
        
    @property
    def theorem37()->str:
        return '''
        Theorem 3.7 Dirichlet. If a and b are relatively prime positive integers,
        then the arithmetic progression
                a, a + b, a + 2b, a + 3b, ...
        contains infinitely many primes.
        '''

    @property
    def theorem38()->str:
        return '''
        Theorem 3.8. If all the n > 2 terms of the arithmetic progression
                p, p + d, p + 2d, ... , p + (n - l)d
        are prime numbers, then the common differenced is divisible by every prime q < n.
        '''


if __name__ == '__main__':
    d = Divisibility()
    print(math.gcd(111, 12))
    print(d.lcm(111, 12))
    p = Prime()
    print(p.is_prime(147))
    print(p.is_square(147), p.is_square(100))