# 두 정수 사이의 합
def solution(a, b):
    a, b = min(a, b), max(a, b)
    return (b - a + 1) * (a + b) // 2