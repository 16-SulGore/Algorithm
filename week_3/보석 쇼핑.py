from collections import defaultdict

def solution(gems):
    n, k = len(gems), len(set(gems))
    
    counter = defaultdict(int)
    subset = set()
    start = 0
    end = -1
    answer = [0, n]
    while start < n and end < n:
        if end - start < answer[1] - answer[0] and len(subset) == k:
            answer = [start + 1, end + 1]
        if end < n - 1 and len(subset) != k:
            end += 1
            counter[gems[end]] += 1
            subset.add(gems[end])
        else:
            counter[gems[start]] -= 1
            if not counter[gems[start]]:
                subset.discard(gems[start])
            start += 1
    
    return answer