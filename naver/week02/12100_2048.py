from collections import deque

EMPTY = 0
DIRECTIONS = (1, 0), (0, 1), (-1, 0), (0, -1)


def getNextSpot(dx, dy, i, j):
    if dx + dy > 0:
        nx = dx * i + dy * j
        ny = dy * i + dx * j
    else:
        nx = N - 1 + dx * i + dy * j
        ny = N - 1 + dy * i + dx * j
    return nx, ny


def createInitDeque(direction, board):
    dx, dy = direction
    dq = deque()
    for i in range(N):

        line = deque()
        for j in range(N):
            nx, ny = getNextSpot(dx, dy, i, j)

            if board[nx][ny] != EMPTY:
                line.append(board[nx][ny])

        dq.append(line)
    return dq


def insertDequeInBoard(direction, dq):
    dx, dy = direction
    new_board = [[EMPTY] * N for _ in range(N)]
    for i in range(N):

        line = dq.popleft()
        for j in range(N):
            nx, ny = getNextSpot(dx, dy, i, j)

            new_board[nx][ny] = line.popleft() if line else EMPTY
    return new_board


def addBoard(dq):
    new_deque = deque()
    while dq:
        dq_line = deque()
        line = dq.popleft()
        end = EMPTY

        if line:
            end = line.popleft()

        while line:
            top = line.popleft()
            if end == top:
                if end != EMPTY:
                    dq_line.append(end * 2)
                end = EMPTY
            else:
                if end != EMPTY:
                    dq_line.append(end)
                end = top

        if end != EMPTY:
            dq_line.append(end)
        new_deque.append(dq_line.copy())
    return new_deque


def move(depth, direction, board):
    if depth == 5:
        return max([max(line) for line in board])

    dq = createInitDeque(direction, board)
    new_board = insertDequeInBoard(direction, addBoard(dq))

    return max([move(depth + 1, new_direction, new_board) for new_direction in DIRECTIONS])


N = int(input())
origin_board = [list(map(int, input().split())) for _ in range(N)]
print(max([move(0, direction, origin_board) for direction in DIRECTIONS]))
