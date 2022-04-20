from itertools import chain, combinations

def has_uniqueness(relation, attributes):
    instances = set(tuple(map(lambda x: column[x], attributes)) for column in relation)
    return len(instances) == len(relation)

def has_minimality(candidates, attributes):
    attributes = set(attributes)
    subset_checks = list(map(lambda x: set(x).issubset(attributes), candidates))
    return subset_checks.count(True) == 0

def solution(relation):
    row_length = len(relation[0])
    cases = chain(*map(lambda x: combinations(range(row_length), x), range(1, row_length + 1)))
    candidates = set()
    for case in cases:
        if has_minimality(candidates, case) and has_uniqueness(relation, case):
            candidates.add(case)
    
    return len(candidates)
