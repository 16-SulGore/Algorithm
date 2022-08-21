# Ex_16236 아기상어

from collections import deque

# global const
EMPTY = 0
SIZE = (1, 2, 3, 4, 5, 6)
ENEMY = 9
dx = -1, 0, 0, 1
dy = 0, -1, 1, 0


def getEnemySpot():
    for x in range(N):
        for y in range(N):
            if board[x][y] == ENEMY:
                return x, y


def canMove(x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] <= enemy_size


def isPriority(ex, ey, x, y, edis, dis):
    return x < ex or (x == ex and y < ey) or dis < edis


def getNextSpot(x, y):
    dq = deque()
    dq.append([x, y, 0])
    visited = [[False] * N for _ in range(N)]
    answer = -1, -1, N * N  # x, y, distance
    while dq:
        x, y, distance = dq.popleft()

        if not visited[x][y]:
            visited[x][y] = True

            if board[x][y] in SIZE and board[x][y] < enemy_size and distance <= answer[2]:
                if isPriority(answer[0], answer[1], x, y, answer[2], distance):
                    answer = x, y, distance

            else:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if canMove(nx, ny):
                        dq.append([nx, ny, distance + 1])
    return answer


# input
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
enemy_size = 2
time = 0
eat_stack = 0

dq = deque()
dq.append(getEnemySpot())
while dq:
    x, y = dq.popleft()
    nx, ny, dis = getNextSpot(x, y)

    if nx != -1:
        board[nx][ny] = ENEMY
        board[x][y] = EMPTY
        time += dis
        eat_stack += 1

        if eat_stack == enemy_size:
            eat_stack = 0
            enemy_size += 1

        dq.append([nx, ny])

print(time)
