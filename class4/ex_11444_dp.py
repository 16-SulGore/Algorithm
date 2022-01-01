# Ex_11444 피보나치 수 6 [골3]
# dp를 사용하고자 n칸을 차지하는 배열을 초기화할 때 메모리가 초과된다.
# 행렬의 곱셈을 이용

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

def solution(n):
    bin_n = bin(n)[2:]
    result = Matrix()
    result.set_unit_matrix()
    
    power_dp = [Matrix()] * (len(bin_n) + 1)
    for i in range(len(bin_n)):
        power_dp[i + 1] = power_dp[i].mul_matrix(power_dp[i])
    
    for i in range(len(bin_n)):
        if bin_n[-i - 1] == '1':
            result = result.mul_matrix(power_dp[i])

    return result.b


if __name__ == "__main__":
    print(solution(int(input())))
