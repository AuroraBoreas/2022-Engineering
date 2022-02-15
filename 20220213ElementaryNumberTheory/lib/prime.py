

from typing import List


class Prime:
    @property
    def what()->str:
        '''
        prime vs composite
        '''
        return 'an integer p > 1 is called a prime, if its only positive divisors are 1 and p;'

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

if __name__ == '__main__':
    p = Prime.eratosthenes(132)
    print(p)