# time limit

def solution(A, B, C):
    result = 0
    for num in (A, B, C, A | B | C):
        result += pow(2, bin(num)[2:].count('0'))

    for num in (A | B, B | C, C | A):
        result -= pow(2, bin(num)[2:].count('0'))

    return result
