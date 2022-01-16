# [1차] 비밀지도
def padding(n, x):
    while len(x) < n:
        x = ' ' + x
    return x

def solution(n, arr1, arr2):
    return [padding(n, bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' ')) for i in range(n)]