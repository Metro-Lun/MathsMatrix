import random

"""CLASS"""

class Matrix :

    def __init__(self, lines=1, columns=1) :
        self.mat = [[0]*columns for i in range(lines)]
        self.lines = lines
        self.cols = columns

    def __repr__(self) :
        ch = ""
        for i in range(len(self.mat)) :
            for elt in self.mat[i] :
                ch += f"{elt} "
            if i != len(self.mat)-1 :   # to avoid an extra space
                ch += "\n"
        return ch

    def change(self, pos, val) :  # changes a value in the matrix
        if type(pos) != tuple :
            return "Can't find the position."
        self.mat[pos[0]-1][pos[1]-1] = val

    def fill(self, val) :     # changes all values to the same one
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                self.mat[i][j] = val
    
    def random_fill(self) :       # changes all values to random numbers
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                self.mat[i][j] = random.randint(0,30)

    def det(self) :     #for now, only for matrices of dimension(2,2)
        return self.mat[0][0]*self.mat[0][1] + self.mat[1][0]*self.mat[1][1]

    def is_invertible(self) :       # for now, only for matrices of dimension(2,2)
        if self.lines == self.cols == 2 :
            if self.det != 0 :
                return True
        return False
            
"""FUNCTIONS"""

def sum(A,B) :
    if A.lines == B.lines and A.cols == B.cols :
        C = Matrix(A.lines,A.cols)
        for i in range(len(C.mat)) :
            for j in range(len(C.mat[i])) :
                C.mat[i][j] = A.mat[i][j] + B.mat[i][j]
        return C
    else :
        return "The matrices do not have the same dimensions."

def s_product(A,val) :      # product of a matrix and a scalar
    C = A
    for i in range(len(A.mat)) :
            for j in range(len(A.mat[i])) :
                C.mat[i][j] = C.mat[i][j]*val
    return C