from collections import deque

INF = float("inf")
STRAIGHT_COST = 100
CORNER_COST = 500
DIRECTION = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def solution(board):
    l = len(board)
    dp = [[INF] * l for _ in range(l)]
    
    que = deque([(0, 0, 0, 2)])
    while que:
        x, y, cost, way = que.popleft()

        is_in = 0 <= x < l and 0 <= y < l
        if not is_in or dp[y][x] < cost or board[y][x]:
            continue
        
        dp[y][x] = cost
        for dx, dy in DIRECTION:
            dway = abs(dx) - abs(dy)
            has_corner = abs(way + dway) < 1
            plus_cost = STRAIGHT_COST + has_corner * CORNER_COST
            que.append((x + dx, y + dy, cost + plus_cost, dway))
    
    return dp[-1][-1]