
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
        Definition 6.2. A number-theoretic function f is said to be multiplicative
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
        Theorem 6.3. The functions r and <J are both multiplicative functions.
        '''

    
    