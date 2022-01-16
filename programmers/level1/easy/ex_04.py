# 문자열 내 p와 y의 개수 비교하기

def solution(s):
    return s.count('p') + s.count('P') == s.count('y') + s.count('Y')