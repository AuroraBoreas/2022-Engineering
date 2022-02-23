
class NumberTheoreticFunctions:
    @property
    def what()->str:
        return '''
        Definition 6.1. Given a positive integer n, let τ(n) denote the number of positive
        divisors of n and σ(n) denote the sum of these divisors

        for example,
        consider n = 12, divisors = (1, 2, 3, 4, 6, 12);

        τ(12) = 6
        σ(12) = 28

        evidently, if p is a prime,
        then τ(p) = 2, σ(p) = p + 1
        '''

    @property
    def definition()->str:
        return '''
        Definition 6.2. A number-theoretic function f is said to be "multiplicative"
        if f(mn) = f(m)f(n), whenever gcd(m , n) = 1.
        '''

    @property
    def theorem61()->str:
        return '''
        Theorem 6.1. If n = p1^k1 p2^k2 • • • pr^kr' is the prime factorization of n > 1, 
        then the positive divisors of n are precisely those integers d of the form
                d = p1^a1 p2^a2 · · · Pr^ar
        where 0 <= ai <= ki (i = 1, 2, ... , r).
        '''

    @property
    def theorem62()->str:
        return '''
        Theorem 6.2. If n = p1^k1 p2^k2· ·· pr^kr' is the prime factorization of n > 1,  then
            (a) τ(n) = (k1 + l)(k2 + 1)· · · (kr + 1) = Π(ki + 1), where 1 <= i <= r
            (b) σ(n) = (p1^(k1+1)-1)/(p1-1) (p2^(k2+1)-1)/(p2-1) (pr^(r+1)-1)/(pr-1) = Π((pi^(ki+1)-)/(pi-1)), where 1 <= i <= r
        '''

    @property
    def theorem63()->str:
        return '''
        Theorem 6.3. The functions τ and σ are both multiplicative functions.
        '''
    @property
    def theorem64()->str:
        return '''
        Theorem 6.4. If f is a multiplicative function and F is defined by
            F(n) = Σ(d|n) f(d) 

        then F is also multiplicative.
        '''
    @property
    def mobius()->str:
        return '''
        Definition 6.3. For a positive integer n, defineμ by the rules
             1       if n = 1
        μ(n) 0       if p^2 | n for some prime p
             (-n)^r  if n = p1p2...pr, where pi are distinct primes
        '''
    
    @property
    def theorem()->str:
        return '''
        Theorem 6.5. The function μ is a multiplicative function.
            μ(mn) = μ(m)μ(n)    
        '''

    @property
    def theorem66()->str:
        return '''
        Theorem 6.6. For each positive integer n >= 1,
                        1 if n = 1
        Σ(d|n) μ(d) = 
                        0 if m = 0
        '''

    @property
    def mobius_inversion_formula()->str:
        return '''
        Theorem 6.7 Mobius inversion formula. Let F and f be two number-theoretic
        functions related by the formula
            F(n) = Σ(d|n) f(d)

        then
            f(n) = Σ(d|n) μ(d)F(n/d) = Σ(d|n) μ(n/d)F(d)

        when n >= 1

        1 = Σ(d|n) μ(n/d) τ(d)
        n = Σ(d|n) μ(n/d) σ(d)
        '''

    @property
    def theorem68()->str:
        return '''
        Theorem 6.8. If F is a multiplicative function and
            F(n) = Σ(d|n) f(d)

        then f is also multiplicative.
        '''

    @property
    def greatest_integer_function()->str:
        return '''
        Definition 6.4. For an arbitrary real number x, we denote by [x] the largest integer
        less than or equal to x; 
        
        that is, [x] is the unique integer satisfying x - 1 < [x] <= x.
        '''

    @property
    def theorem69()->str:
        return '''
        Theorem 6.9. If n is a positive integer and p a prime, then the exponent of the highest
        power of p that divides n! is
            Σ(1<= κ <= inf) [n / p^k]

        where the series is finite, because [n / p^k] = 0 for p^k > n.
        '''

    @property
    def theorem610()->str:
        return '''
        Theorem 6.10. If n and r are positive integers with 1 <= r < n,
        then the binomial coefficient
                          n!
            (n r)  = -----------
                      r! (n-r)!

        is also an integer
        '''

    