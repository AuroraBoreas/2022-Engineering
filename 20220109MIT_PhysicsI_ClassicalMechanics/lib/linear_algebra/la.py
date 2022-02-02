
class LinearAlgebra:
    '''
    + - x

    scalar

    A ^ -1

    A ^ T

    Eigenvector & Eigenvalue

    • dot product

    '''

    @property
    def linear_equation(self)->str:
        '''
        what
        '''
        return '多元一次'

    @property
    def matrix(self)->str:
        '''
        3x + 2y - 1z = 3

        x  - 4y + 4z = 2

                  6z = 0

        3 2 -1 3

        1 -4 4 2

        0 0  6 0
        '''
        return '[...]'

    @property
    def augment_matrix(self)->str:
        return '[....]'

    @property
    def scalar(self)->str:
        return 'c•[...] = [...]'

    @property
    def rref(self)->str:
        '''
        what is rref?

        indentify matrix (单位矩阵)

        - leading 1s

        - only 0s above 1s

        - all 0s must be the last row

        1 0 0
        0 1 0
        0 0 1
        '''
        return 'reduced row echelon form'

    @property
    def gaussian_elimination(self)->str:
        return 'gaussian elimination'

    @property
    def vector_equation(self)->str:
        '''
        Av = B;

        [][] = []

        vector: row vector; column vector;
        dimension : 1 x m; m x 1

        vector equation -> linear equation

        geometric meaning: rotate 90 deg in math; rotate -90 deg in computation;

        '''
        return 'vector equation'

    @property
    def matrix_equation(self)->str:
        '''
        matrix equation -> linear equation

        matrix:

        m x r; r x n; m x n

        [] x [] = []

        algorithm: rv = Σωivi

        '''
        return 'matrix equation'

    def transpose(self)->str:
        '''
        geometric meaning:

        []([]A) = [shear][rotate]A = [Composite]A

        '''
        return 'In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal'

    @property
    def determinant(self)->str:
        '''
        alorithm: cross out each column to get multipler recursively; component sign is sequential + - + - ...

        special case: det(triangular matix)
        '''
        return 'determinant algorithm'

    @property
    def trace(self)->str:
        return 'tr(A) = sum(diagonal)'

    @property
    def square_matrix(self)->str:
        '''
        invert

        symmetric

        skew-symmetric

        '''
        return 'square matrix: n x n'

    @property
    def triangular_matrix(self)->str:
        '''
        geometric meaning: diagonal delimiter: 0s on upper or lower of a matrix
        '''
        return 'triangular matrix: upper matrix; lower matrix'

    @property
    def eigenvalue_eigenvector(self)->str:
        '''
        v is eigenvector;

        λ is eigenvalue;

        algorithm to find λ:

        (A - λI)v = o;

        det(A - λI) = 0;

        '''
        return 'Av = λv; where v != o'

    @property
    def dot_product(self)->str:
        '''
        a • b = Σwivi

        a • a >= 0

        Communitive

        Identity

        Associative

        Distributive
        '''
        return 'a • b = Σwivi'

    @property
    def vector_length(self)->str:
        '''
        ||v|| = (v • v) ^ -0.5

        vector property

        unit vector: a vector of length 1

        any vector -> unit vector(cv) is: c = 1 / (||v||)

        '''
        return '||v|| = (Σwi) ^ -0.5'

    @property
    def orthogonal_vector(self)->str:
        '''
        two vectors v and w are said to be orthogonal if v • w = 0

        v is perpendicular to w

        orthogonal set of vectors is a collection of orthogonal vectors

        '''
        return 'v • w = 0'

    @property
    def orthogonal_matrix(self)->str:
        '''
        property

        1. every pair of column vectors is orthogonal;

        2. each column vector length is 1;

        3. A ^ T x A = I (diagonilazing)

        4. A ^ -1 = A ^ T

        theorems:

        1. eigenvalues of a symmetric matrix are real numbers;

        2. eigenvector of a symmetric matrix (corresponding to distinct eigenvalues) are orthogonal;
        '''
        return 'a square matrix with orthogonal column vectors'

    @property
    def diagonalizable(self)->str:
        '''
        A is n x n square matrix

        D is a diagonal matrix D

        P is an invertable matrix
        '''
        return 'A = P D P ^ -1'

    @property
    def linear_combination_of_vectors(self)->str:
        '''
        general concept:

        In linear algebra, we define the concept of linear combinations in terms of vectors.

        But, it is actually possible to talk about linear combinations of anything

        as long as you understand the main idea of a linear combination

        formula: (scalar)(something 1) + (scalar)(something 2) + (scalar)(something 3)

        linear dependent:

        something 1 ... are linearly dependent if scalars exit;

        something 1 ... are linearly independent if scalars are all 0s;

        (scalar)(something 1) + (scalar)(something 2) + (scalar)(something 3) = 0;

        '''
        return '(scalar)(something 1) + (scalar)(something 2) + (scalar)(something 3)'

    @property
    def singular_value_decomposition(self)->str:
        '''
        A is m x n matrix;

        V ^ T = V ^ -1;

        Σ is m x n diagonal matrix

        V is n x m orthogonal matrix

        SVD of A = U Σ V ^ T; or SVD of A = U Σ V ^ -1;

        algorithm: to find U Σ V ?

        step1: find A^T A (n x n matrix); (A^T A)^T = A^T(A^T)^T = A^T A;
        step2: skip

        '''
        return '[A] = [U] [Σ] [V] ^ T; [A] = [U] [Σ] [V] ^ -1'
