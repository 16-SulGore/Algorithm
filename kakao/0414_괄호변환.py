# 균형잡힌 -> 올바른
from enum import Enum

class Bracket(Enum):
    OPEN = "("
    CLOSE = ")"

def solution(p):
    return convert(p)

def convert(w):
    result = ""

    # 1
    if w == "":
        return ""
    
    # 2
    u, v = split_str(w)

    # 3
    if is_right_str(u):
        result += u + convert(v)
        
    # 4
    else:
        new_str = "(" + convert(v) + ")"
        return new_str + reverse_bracket(u[1:-1])
    
    return result
        
def split_str(str):
    balance_str = ""
    for i in range(len(str)):
        balance_str += str[i]
        
        if is_balanced_str(balance_str):
            return balance_str, str[i + 1:]
        
    return balance_str, str

def is_balanced_str(str):
    return str.count(Bracket.CLOSE.value) == str.count(Bracket.OPEN.value)

def is_right_str(str):
    stack = []
    for char in str:
        if char == Bracket.OPEN.value:
            stack.append(True)
        else:
            if stack:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0

def reverse_bracket(str):
    result = ""
    for char in str:
        result += Bracket.CLOSE.value if char == Bracket.OPEN.value else Bracket.OPEN.value
    return result
