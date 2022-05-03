from collections import deque

def solution(board):
    n = len(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(n)]
    dp[0][0] = [0, 0, 0, 0]

    q = deque([(0, 0, -1)])
    while q:
        i, j, d = q.popleft()
        for nd, (di, dj) in enumerate(directions):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and not board[ni][nj]:
                next_cost = dp[i][j][d] + (100 if d == nd or d == -1 else 600)
                if next_cost < dp[ni][nj][nd]:
                    dp[ni][nj][nd] = next_cost
                    q.append((ni, nj, nd))
    return min(dp[-1][-1])