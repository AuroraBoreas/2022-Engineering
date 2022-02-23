# quadratic reciprocity law deals with the solvability of quadratic congruence.


class QuadraticReciprocityLaw:
    @property
    def what()->str:
        return '''
        
        Definition 9.1. Let p be an odd prime and gcd(a, p) = 1. 
        If the quadratic congruence x^2 ≡ a (mod p) has a solution, 
        then a is said to be a quadratic residue of p. 
        Otherwise, a is called a quadratic nonresidue of p.


        The point to bear in mind is that if a ≡ b (mod p), 
        then a is a quadratic residue of p if and only if bis a quadratic residue of p. 
        Thus, we only need to determine the quadratic character of those positive integers less than p to ascertain that of any integer.
        '''