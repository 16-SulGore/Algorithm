from itertools import combinations

def is_unique(combination, relation):
    return len(relation) == len(set(tuple([r[c] for c in combination]) for r in relation))

def check_minimality(all_combination, visited, i):
    for j in range(len(all_combination)):
        if not visited[j] and all_combination[i].issubset(all_combination[j]):
            visited[j] = 1

def solution(relation):
    all_combination = [set(combination) for i in range(1, len(relation[0]) + 1) for combination in combinations(range(len(relation[0])), i)]
    visited = [0 for _ in range(len(all_combination))]
    answer = 0
    for i in range(len(all_combination)):
        if not visited[i]:
            if is_unique(all_combination[i], relation):
                answer += 1
                check_minimality(all_combination, visited, i)
    return answer