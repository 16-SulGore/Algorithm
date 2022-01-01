# Ex_1918 후위 표기식 [골3]
# Tree 방식을 사용하려 했으나, 수식 트리를 만들기 위해서는 먼저 후위 표기식으로 바꿀 필요가 있다.
# 후위 표기식으로 변환하는 방식을 정확히 이해하지 못했다.

def solution(notation):
    result = ""
    stack = []
    
    for c in notation:
        if c.isalpha():
            result += c
        
        elif c == '(':
            stack.append(c)
            
        elif c == ')':
            # 이전 괄호가 열렸을 때까지의 모든 연산을 진행한다.
            while stack and stack[-1] != '(':
                result += stack.pop()    
            stack.pop() # 여는괄호 제거
            
        elif c == '*' or c == '/':
            # 1순위 연산은 1순위 연산만을 이어서 진행한다.
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(c)

        elif c == '+' or c == '-':
            # 2순위 연산은 1순위와 2순위 연산 모두 연달아 진행한다.
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(c)
    
    while stack:
        result += stack.pop()
    return result

if __name__ == "__main__":
    print(solution(input()))