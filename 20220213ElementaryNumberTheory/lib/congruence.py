
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

    @property
    def fermat_theorem()->str:
        '''
        Theorem 5.1 Fermat's theorem.
        '''
        return '''
        Let p be a prime and suppose that p ~| a. Then a^(p-l) ≡ 1 (mod p).

        corollary.
        If p is a prime, then a^p ≡ a (mod p) for any integer a.

        Lemma. 
        If p and q are distinct primes with a^p ≡ a (mod q) and a^q ≡ a (mod p),
        then a^pq ≡ a (mod pq).

        '''
    
    @property
    def theorem52()->str:
        return '''
        Theorem 5.2. If n is an odd pseudoprime, then Mn = 2^n - 1 is a larger one.
        '''

    @property
    def theorem53()->str:
        return '''
        Theorem 5.3. Let n be a composite square-free integer, say, n = p1p2 · · · pr,
        where the pi are distinct primes. If pi - 1 | n - 1 for i = 1, 2, ..., r,
        then n is an absolute pseudoprime.
        '''
    @property
    def wilson()->str:
        '''
        P105/451
        '''
        return '''
        If p is a prime, then (p - 1)! ≡ - 1 (mod p).
        '''

    @property
    def theorem55()->str:
        return '''
        Theorem 5.5. The quadratic congruence x^2 + 1 ≡ 0 (mod p), where p is an odd prime, 
        has a solution if and only if p ≡ 1 (mod 4).
        '''

    @property
    def fermat_factoring_method()->str:
        return '''
        If n is the difference of two squares, then it is apparent that n can be factored as
                n = x^2 - y^2 = (x + y )(x - y)
        
        Conversely, when n has the factorization n = ab, with a >= b >= 1, then we may write
                n = ((a + b)/2)^2 - ((a - b)/2)^2

        step1: determine the smallest int k for which k^2 >= n;
        step2: look successively at numbers m = 
                k^2 - n,
                (k+1)^2 - n,
                ...
        step3: m >= sqrt(n) is found (m^2 - n) a square
        
        why: convergence at
                ((n + 1)/2)^2 - n = ((n + 1)/2)^2
        
        note: how to check a number could be a squre?
        final digit must within {0, 1, 4, 5, 6, 9}
        '''