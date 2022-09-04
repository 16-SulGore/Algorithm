import sys
sys.setrecursionlimit(100000)

class Matrix:
    def __init__(self, a = 1, b = 1, c = 1, d = 0) -> None:
        self.a = a # Fn+1
        self.b = b # Fn
        self.c = c # Fn
        self.d = d # Fn-1
    
    def set_unit_matrix(self):
        self.a = 1
        self.b = 0
        self.c = 0
        self.d = 1
        
    def mul_matrix(self, other):
        a = (self.a * other.a + self.b * other.c) % 1000000007
        b = (self.a * other.b + self.b * other.d) % 1000000007
        c = (self.c * other.a + self.d * other.c) % 1000000007
        d = (self.c * other.b + self.d * other.d) % 1000000007
        
        return Matrix(a, b, c, d)


def power_of_matrix(matrix, bin_n):    
    if bin_n == "1":
        return Matrix()

    half = power_of_matrix(matrix, bin_n[:-1])
    
    if bin_n[-1] == '1':
        return half.mul_matrix(Matrix()).mul_matrix(half)

    else:
        return half.mul_matrix(half)

def solution(n):
    bin_n = bin(n)[2:]
    return power_of_matrix(Matrix(), bin_n).b


if __name__ == "__main__":
    print(solution(int(input())))