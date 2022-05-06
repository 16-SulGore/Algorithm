def solution(gems):
    n, k = len(gems), len(set(gems))
    types = set([gems[0]])
    start = end = 0
    answer = [0, n]
    while start < n and end < n:
        if end - start < answer[1] - answer[0] and len(types) == k:
            answer = [start, end]
        if end < n - 1 and len(types) != k:
            end += 1
            types.add(gems[end])
        else:
            start += 1
            types = set(gems[start:end + 1])
    
    return [answer[0] + 1, answer[1] + 1]