def solution(n):
    result, count = 0, 0
    for bit in bin(n)[2:]:
        result, count = (max(result, count), 0) if bit == '1' else (result, count + 1)
    return result
