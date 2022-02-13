import dataclasses

@dataclasses.dataclass
class Priliminary:
    takeaway:str = 'An understanding of the stmt of a theorem, not the proof, is the important issue'
    wop:str = "well-ordered principle"
    archimedean_property:str = "n*a >= b, where a, b, n ∈ Positive Integer;"

    @property
    def first_principle_of_finite_induction(self)->str:
        return 'let S be a set of positive integers with the following properties:' \
        + '\n(a) the integer 1 belongs to S;' \
        + '\n(b) whenever the integer k is in S, then next integer k+1 must also be in S;' \
        + '\n\n=> Then S is the set of all positive integers.'

    @staticmethod
    def sum_of_square_n(n:int)->float:
        '''
        sum = 1^2 + 2^2 + 3^2 + ... + n^2
        '''
        return n * (n * 2 + 1) * (n + 1) / 6

    @staticmethod
    def sum_of_square_n2(n:int)->float:
        return 2 ** n - 1

    def n_factorial(self, n:int)->int:
        return 1 if n < 2 else n * self.n_factorial(n - 1)

    @property
    def second_principle_of_finit_induction(self)->str:
        '''
        easier version
        '''
        return 'let S be a set of positive integers with the following properties:' \
        + '\n(a) the integer 1 belongs to S;' \
        + '\n(b\') if k is a positive integer such that 1,2,...,k belong to S, then k+1 must also be in S;' \
        + '\n\n=> Then S is the set of all positive integers.'

if __name__ == '__main__':
    p:Priliminary = Priliminary()
    print(p.first_principle_of_finite_induction)
