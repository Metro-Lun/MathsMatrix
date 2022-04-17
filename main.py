import random
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
        
    def __add__(self,other) :
        if self.lines == other.lines and self.cols == other.cols :
            sum = Matrix(self.lines,self.cols)
            for i in range(len(sum.mat)) :
                for j in range(len(sum.mat[i])) :
                    sum.mat[i][j] = self.mat[i][j] + other.mat[i][j]
            return sum
        else :
            return "The matrices do not have the same dimensions."

    def __mul__(self,other) :
        if type(other) == int :     # product of a matrix and a scalar
            prdt = self
            for i in range(len(self.mat)) :
                for j in range(len(self.mat[i])) :
                    prdt.mat[i][j] = prdt.mat[i][j]*other
            return prdt
    
    def fill(self, val) :     # changes all values to the same one
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                self.mat[i][j] = val
    
    def random_fill(self) :       # changes all values to random numbers
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                self.mat[i][j] = random.randint(0,10)

    def det(self) :     #for now, only for matrices of dimension(2,2)
        return self.mat[0][0]*self.mat[1][1] - self.mat[1][0]*self.mat[0][1]

    def is_invertible(self) :       # for now, only for matrices of dimension(2,2)
        if self.lines == self.cols == 2 :
            if self.det() != 0 :
                return True
        return False
            
    def inverse(self) :
        if self.is_invertible() :       # means that det(self) != 0
            A1 = Matrix(self.lines,self.cols)
            A2 = Matrix(self.lines,self.cols)
            
            temp = self.mat[0][0]
            A1.mat[0][0] = self.mat[1][1]
            A1.mat[0][1] = -self.mat[0][1]
            A1.mat[1][0] = -self.mat[1][0]
            A1.mat[1][1] = temp

            coef = round(1/self.det(),3)
            A2 = s_product(A1,coef)
            return A2
        else :
            return "The matrix is not invertible."

    def is_identity(self) :     # bool
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                if i != j :
                    if self.mat[i][j] != 0 : return False
                if i == j :
                    if self.mat[i][j] != 1 : return False
        return True