from collections import deque

POINT_X = (0, 1, 0, 1)
POINT_Y = (0, 0, 1, 1)
EMPTY_BLOCK = '#'

def match_list(m, n, board):
    matches = []
    for y in range(m - 1):
        for x in range(n - 1):
            block_types = set(map(lambda dx, dy: board[y + dy][x + dx], POINT_X, POINT_Y))
            if len(block_types) == 1 and board[y][x] != EMPTY_BLOCK:
                matches.append((x, y))
    
    return matches

def remove_blocks(m, n, board, matches):
    count = 0
    
    for x, y in matches:
        for dx, dy in zip(POINT_X, POINT_Y):
            board[y + dy][x + dx] = EMPTY_BLOCK
    
    for x in range(n):
        dq = deque()
        for y in range(m):
            block = board[y][x]
            if block == EMPTY_BLOCK:
                dq.append(block)
                count += 1
            else:
                dq.appendleft(block)
        
        for y in range(m):
            board[y][x] = dq.pop()
    
    return count

def solution(m, n, board):
    board = list(map(list, board))
    answer = 0
    
    while True:
        matches = match_list(m, n, board)
        if not len(matches):
            break
        answer = remove_blocks(m, n, board, matches)
    
    return answer