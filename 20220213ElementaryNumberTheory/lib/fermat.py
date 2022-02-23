
class Fermat:
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
