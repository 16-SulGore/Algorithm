from collections import deque

INF = float("inf")
STRAIGHT_COST = 100
CORNER_COST = 500
DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Point:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction
        
def solution(board):
    n = len(board)
    dp = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    dp[0][0] = [0, 0, 0, 0]
    que = deque([Point(0, 0, -1)])
    while que:
        target = que.popleft()
        target_cost = dp[target.y][target.x][target.dir]

        for direction, (dx, dy) in enumerate(DIRECTION):
            x, y = target.x + dx, target.y + dy
            has_corner = (direction != target.dir) and (target.dir >= 0)
            cost = target_cost + STRAIGHT_COST + has_corner * CORNER_COST
            
            is_in = 0 <= x < n and 0 <= y < n
            if not is_in or board[y][x] or dp[y][x][direction] <= cost:
                continue
            
            dp[y][x][direction] = cost
            que.append(Point(x, y, direction))
    
    return min(dp[-1][-1])