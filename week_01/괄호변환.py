def check_bracket_balance(u):
    stack = []
    for bracket in u:
        if bracket == '(':
            stack.append(0)
        else:
            stack and stack.pop()
    return len(stack) == 0

def reverse_bracket(u):
    return ''.join([')' if bracket == '(' else '(' for bracket in u])

def solution(w):
    if not w:
        return w
    u = v = ''
    bracket_cnt = [0, 0]
    for i in range(len(w)):
        if w[i] == '(':
            bracket_cnt[0] += 1
        elif w[i] == ')':
            bracket_cnt[1] += 1
        u += w[i]
        if bracket_cnt[0] == bracket_cnt[1]:
            v = w[i+1:]
            break

    if check_bracket_balance(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse_bracket(u[1:-1])