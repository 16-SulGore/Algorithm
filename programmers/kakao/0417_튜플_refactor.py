from functools import reduce

def solution(s):
    return reduce(lambda acc, cur: acc + list(set(cur) - set(acc)), parse(s))

def parse(str):
    splited_with_bracket = str[2:-2].split("},{")
    splited_with_comma = lambda splited: list(map(int, splited.split(",")))
    splited_list = [splited_with_comma(splited) for splited in splited_with_bracket]

    return sorted(splited_list, key= lambda x: len(x))