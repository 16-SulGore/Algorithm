from itertools import permutations
from collections import deque
import copy

class Node:
    def __init__(self, opcode, left = None, right = None):
        self.opcode = opcode
        self.calculate = self.get_calculator()
        self.left = left
        self.right = right

    def get_calculator(self):
        if self.opcode == '+':
            return lambda a, b: a + b
        elif self.opcode == '-':
            return lambda a, b: a - b
        elif self.opcode == '*':
            return lambda a, b: a * b

def solution(expression):
    operator_nodes, opcodes = get_operator_nodes(expression)
    max_result = get_max_result(operator_nodes, opcodes)
    return max_result

def get_operator_nodes(expression):
    operators, opcodes, num = [], set(), ''
    for expr in expression + '!':
        if expr.isdigit():
            num += expr
            continue
        operand = int(num)
        if operators:
            operators[-1].right = operand
        if expr in ('-', '+', '*'):
            opcodes.add(expr)
            operator = Node(expr, left = operand)
            operators.append(operator)
        num = ''
    return operators, opcodes

def get_max_result(operator_nodes, opcodes):
    max_result = 0
    for now_opcode in permutations(opcodes, len(opcodes)):
        max_result = max(max_result, abs(calculate(operator_nodes, now_opcode)))
    return max_result

def calculate(operator_nodes, opcodes):
    before_comparison = deque(copy.deepcopy(operator_nodes))
    after_comparison = deque()
    result = 0
    for opcode in opcodes:
        while before_comparison:
            operator = before_comparison.popleft()
            if opcode == operator.opcode:
                num = operator.calculate(operator.left, operator.right)
                if after_comparison:
                    after_comparison[-1].right = num
                if before_comparison:
                    before_comparison[0].left = num
                result = num
                continue
            after_comparison.append(operator)
        before_comparison, after_comparison = after_comparison, before_comparison
    return result