import re
from itertools import permutations

def compute(expression, priority):
    expression = expression[:]
    for target_op in priority:
        i = 1
        while i < len(expression):
            op = expression[i]
            if op == target_op:
                a = expression[i - 1]
                b = expression.pop(i + 1)
                op = expression.pop(i)
                expression[i - 1] = str(eval(a + op + b))
            else:
                i += 1

    return int(expression[0])
    
def solution(expression):
    expression = re.sub('[\+\-\*]', ' \g<0> ', expression).split()
    
    result = 0
    for priority in permutations(['+', '-', '*'], 3):
        result = max(result, abs(compute(expression, priority)))

    return result