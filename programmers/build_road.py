# 카카오 기출: 경주로 건설
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def solution(board):
    answer = -1
    n = len(board)
    q = deque()
    visited = [[-1 for _ in range(n)]for _ in range(n)]
    q.append([0,0,'.',0])
    while q:
        x, y, d, c = q.popleft() # d = direction, c = cost
        
        if (x,y) == (n-1,n-1) and (answer == -1 or answer > c):
            answer = c

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny]:
                continue
            cost = c + (100 if d == '.' or d == i else 600)
            if visited[nx][ny] != -1 and visited[nx][ny] < cost - 300:
                continue
            q.append([nx,ny,i,cost])
            visited[nx][ny] = cost

    return answer