
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
        (e) If a ≡ b (mod n), then a + c ≡ b + c (mod n) and ac ≡ be (mod n).
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
        of the positive integer N, 0 <= ak < 10, and let S = a0 + a1 +···+am. 
        
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