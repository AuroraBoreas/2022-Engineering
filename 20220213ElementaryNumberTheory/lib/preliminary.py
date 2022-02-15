import dataclasses
import math

@dataclasses.dataclass
class Preliminary:
    takeaway:str = 'An understanding of the stmt of a theorem, not the proof, is the important issue'
    wop:str = "well-ordered principle"
    archimedean_property:str = "n*a >= b, where a, b, n ∈ Positive Integer;"

    @property
    def first_principle_of_finite_induction(self)->str:
        return 'let S be a set of positive integers with the following properties:' \
        + '\n(a) the integer 1 belongs to S;' \
        + '\n(b) whenever the integer k is in S, then next integer k+1 must also be in S;' \
        + '\n\n=> Then S is the set of all positive integers.'

    @property
    def second_principle_of_finit_induction(self)->str:
        '''
        easier version
        '''
        return 'let S be a set of positive integers with the following properties:' \
        + '\n(a) the integer 1 belongs to S;' \
        + '\n(b\') if k is a positive integer such that 1,2,...,k belong to S, then k+1 must also be in S;' \
        + '\n\n=> Then S is the set of all positive integers.'

    def n_factorial(self, n:int)->int:
        '''
        ? = n!
        
        where n ∈ S, S is a set of positive integer;
        '''
        return 1 if n < 2 else n * self.n_factorial(n - 1)

    @staticmethod
    def sum_of_n(n:int)->float:
        '''
        ? = 1 + 2 + 3 + ... + n
        
        where n ∈ S, S is a set of positive integer;
        '''
        return n * (n + 1) / 2

    @staticmethod
    def sum_of_2n_minus_1(n:int)->float:
        '''
        ? = 1 + 3 + 5 + ... + (2n-1)
        
        where n ∈ S, S is a set of positive integer;
        '''
        return n ** 2

    @staticmethod
    def sum_of_square_n(n:int)->float:
        '''
        ? = 1^2 + 2^2 + 3^2 + ... + n^2

        where n ∈ S, S is a set of positive integer;
        '''
        return n * (n * 2 + 1) * (n + 1) / 6

    @staticmethod
    def sum_of_square_n2(n:int)->float:
        return 2 ** n - 1

    @staticmethod
    def sum_of_n_time_n_plus_1(n:int)->float:
        '''
        ? = 1 * 2 + 2 * 3 + 3 * 4 + ... + n * (n + 1)
        
        where n ∈ S, S is a set of positive integer;
        '''
        return n * (n + 1) * (n + 2) / 3

    @staticmethod
    def sum_of_square_2n_minus_1(n:int)->float:
        '''
        ? = 1 + 3 + 5 + ... + (2n - 1)

        where n ∈ S, S is a set of positive integer;
        '''
        return n * (n * 2 - 1) * (n * 2 + 1) / 3

    @staticmethod
    def sum_of_cube_n(n:int)->float:
        '''
        ? = 1^3 + 2^3 + 3^3 + ... + n^3

        where n ∈ S, S is a set of positive integer;
        '''

        return (n * (n + 1) / 2) ** 2

    @staticmethod
    def binomial_coefficiencts(n:int, k:int)->float:
        '''
        C(n k)

        0 <= k <= n
        '''
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    @staticmethod
    def pascal_rule(n:int, k:int)->bool:
        '''
        Pascal's rule
        '''
        return (Preliminary.binomial_coefficiencts(n, k) + 
                Preliminary.binomial_coefficiencts(n, k - 1) == 
                Preliminary.binomial_coefficiencts(n + 1, k))
                
    @staticmethod
    def pascal_triangle()->str:
        '''
        p19/451
        '''
        return '''
             1  1
            1  2  1
           1  3  3   1
          1  4  6   4   1
         1  5  10  10  5  1
        1  6  15 20  15  6  1
              ...
        '''

    @staticmethod
    def binomial_theorem(a:int, b:int, n:int, k:int)->str:
        '''
        so-called binomial theorem is in reality a formula for the complete expansion of (a + b)^n, n >= 1;

        the questionn is how to predict the coefficients;
        
        a clue lies in the observation of Pascal's triangle;
        '''
        return f"({a} + {b})^{n} = Σ(n k)a^({n-k}) b^({k})"

    @staticmethod
    def newton_identity(n:int, k:int, r:int)->bool:
        '''
        n >= k >= r >= 0
        '''
        return (Preliminary.binomial_coefficiencts(n, k) *
                Preliminary.binomial_coefficiencts(k, r) ==
                Preliminary.binomial_coefficiencts(n, r) *
                Preliminary.binomial_coefficiencts(n-r, k-r))

if __name__ == '__main__':
    p:Preliminary = Preliminary()
    print(p.first_principle_of_finite_induction)
