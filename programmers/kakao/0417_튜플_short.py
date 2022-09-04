from functools import reduce

def solution(s):
    return reduce(lambda a, b: a + list(set(b) - set(a)), sorted([list(map(int, n.split(","))) for n in s[2:-2].split("},{")], key= lambda x: len(x)))