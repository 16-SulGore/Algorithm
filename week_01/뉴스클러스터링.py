from collections import Counter

def str_to_elements(str):
    return [str[i:i+2].upper() for i in range(len(str) - 1) if str[i:i+2].isalpha()]

def solution(str1, str2):
    A = Counter(str_to_elements(str1))
    B = Counter(str_to_elements(str2))
    
    intersection = 0
    for element in A:
        if B.get(element, 0):
            intersection += min(A.get(element), B.get(element))

    union = 0
    for element in (A + B).keys():
        union += max(A.get(element, 0), B.get(element, 0))
    
    J = 1 if union == 0 else intersection / union
    return int(J * 65536)