from itertools import combinations

def is_uniqueness(relation, all_combies, row):
    unique = []
    for combi in all_combies:
        if len(set([tuple([r[c] for c in combi]) for r in relation])) == row:
            unique.append(combi)
    return unique

def is_minimality(unique):
    minimality = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i])&set(unique[j])):
                minimality.discard(unique[j])
    return minimality

def solution(relation):
    col, row = len(relation[0]), len(relation)
    
    all_combies = []
    for i in range(1, col + 1):
        all_combies.extend(combinations(range(col),i))
    
    unique = is_uniqueness(relation,all_combies,row)
    candidate_keys = is_minimality(unique)

    return len(candidate_keys)