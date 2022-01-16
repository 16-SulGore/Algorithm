# 크레인 인형뽑기 게임

def solution(board, moves):
    stack = []
    result = 0
    
    for spot in moves:
        for items in board:
            item = items[spot - 1]
            
            if item != 0:
                if stack and stack[-1] == item:
                    stack.pop()
                    result += 2
                else:
                    stack.append(item)
                    
                items[spot - 1] = 0
                break
            
    return result