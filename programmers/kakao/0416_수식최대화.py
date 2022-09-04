OPERATIONS =  ("*", "+", "-")
ORDERS = ((1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1))

def solution(expression):
    return max([get_score(order, parse(expression)) for order in ORDERS])

def parse(expression):
    end = ""
    parsed_list = []
    for char in expression:
        if not char.isdigit():
            parsed_list.append(int(end))
            parsed_list.append(char)

            end = ""
        else:
            end += char

    parsed_list.append(int(end))
    return parsed_list
    
def get_score(order, parsed):
    calculated = parsed[::]
    for i in order:
        calculated = get_calculated_list(OPERATIONS[i - 1], calculated)
    
    return abs(calculated[0]) 

def get_calculated_list(op, parsed):
    if len(parsed) <= 2:
        return parsed

    calculated_list = [parsed[0]]
    for expression in parsed[1:]:
        if calculated_list[-1] == op:
            calculated_list.pop()
            expression = operate(num1= calculated_list.pop(), num2 = expression, op= op)

        calculated_list.append(expression)

    return calculated_list 

def operate(num1, num2, op):
    if op == OPERATIONS[0]:
        return num1 * num2
    elif op == OPERATIONS[1]:
        return num1 + num2
    elif op == OPERATIONS[2]:
        return num1 - num2    