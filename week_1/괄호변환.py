def check_correct(string):
    stacks = 0
    for char in string:
        if char == '(':
            stacks += 1
        if char == ')':
            stacks -= 1
        if stacks < 0:
            return False

    return stacks == 0

def solution(p):
    if not len(p):
        return p
    
    point = 0
    for i in range(len(p)):
        if p[i] == '(':
            point += 1
        if p[i] == ')':
            point -= 1
        if point == 0:
            point = i
            break
    
    u = p[0:point + 1]
    v = p[point + 1:]
    if check_correct(u):
        return u + solution(v)
    
    u = list(u[1:-1])
    for i, char in enumerate(u):
        if char == '(':
            u[i] = ')'
        if char == ')':
            u[i] = '('
        
    return '(' + solution(v) + ')' + ''.join(u)