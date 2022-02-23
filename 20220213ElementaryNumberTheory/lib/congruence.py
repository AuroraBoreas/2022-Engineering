

import math

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

class Congruence:
    @property
    def what()->str:
        return 'a ≡ b (mod n) where a, b, n ∈ Integer; n | a - b'

    @property
    def view_as()->str:
        return 'Congruence may be viewed as a generalized form of equality;' + \
        '\n in the sense that its behavior with respect to addition and multiplication is reminiscent of ordinary equality;'

    @property
    def theorem42()->str:
        return '''
        Let n > 1 be fixed and a, b, c, d be arbitrary integers. 
        Then the following properties hold:

        (a)    a ≡ a (mod n).
        (b) If a ≡ b (mod n), then b ≡ a (mod n).
        (c) If a ≡ b (mod n) and b ≡ c (mod n), then a ≡ c (mod n).
        (d) If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n) and ac ≡ bd (mod n).
        (e) If a ≡ b (mod n), then a + c ≡ b + c (mod n) and ac ≡ bc (mod n).
        (f) If a ≡ b (mod n), then a^k ≡ b^k (mod n) for any positive integer k.
        '''

    @property
    def theorem43()->str:
        return '''
        If ca ≡ cb (mod n), then a ≡ b (mod n/d), where d ≡ gcd(c, n).
        '''

class BinaryDecimal:
    @property
    def theorem44()->str:
        '''
        p82/451
        '''
        return '''
        Let P(x) = Σckxk be a polynomial function of x with integral coefficients ck. 
        If a ≡ b (mod n), then P(a) ≡ P(b) (mod n).
        '''
    
    @property
    def theorem45()->str:
        return '''
        Let N = am 10m + am-110m-1 + · · · + ai 10 + ao, be the decimal expansion 
        of the positive integer N, 0 <= ak < 10, and let S = a0 + a1 + ··· + am. 
        
        Then 9 | N if and only if 9 | S.
        '''

    @property
    def theorem46()->str:
        '''
        p83/451s
        '''
        return '''
        Let N = am 10m + am-110m-1 + · · · + ailO + ao, be the decimal expansion 
        of the positive integer N, 0 <= ak < 10, and let T = ao - a1 + a1 - · · · + (-1)m am. 
        
        Then 11 | N if and only if 11 | T.
        '''

class LinearCongruence:
    @property
    def what()->str:
        return '''
        an equation of the form ax ≡ b (mod n) is called a linear congruence

        and by a solution of such an equation we mean an integer x0 for which ax0 ≡ b (mod n).
        '''

    @property
    def theorem47()->str:
        return '''
        The linear congruence ax ≡ b (mod n) has a solution if and only if d | b, where d = gcd(a, n). 
        
        If d | b, then it has d mutually incongruent solutions modulo n.
        '''
    
    @property
    def theorem48()->str:
        '''
        Theorem 4.8 Chinese Remainder Theorem. 
        '''
        return '''
        Let n 1, n2, ... , nr be positive integers
        such that gcd(ni, nj) = 1 for i != j. Then the system of linear congruences
                            x ≡ ai (mod n1)
                            x ≡ a1 (mod n2)
                                ...
                            x ≡ ar (mod nr)
        has a simultaneous solution, which is unique modulo the integer n1 n2 · · · nr.
        '''

    @property
    def theorem49()->str:
        return '''
        Theorem 4.9. The system of linear congruences
            ax + by ≡ r (mod n)
            ex + dy ≡ s (mod n)
        has a unique solution modulo n whenever gcd(ad - be, n) = 1.
        '''


if __name__ == '__main__':
    d = Diophantine.hassolution(172, 20, 1000)
    d = Diophantine.hassolution(5, 22, 18)
    print(d)