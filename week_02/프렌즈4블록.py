DIRECTION = [(1, 0), (0, 1), (1, 1)]

def get_four_block(m, n, board):
    four_block = [(i, j) for i in range(m) for j in range(n - 1) if board[i][j] and is_four_block(i, j, board, m, n)]
    return four_block

def is_four_block(i, j, board, m, n):
    same_block = [0<= i + di < m and 0 <= j + dj < n and board[i + di][j + dj] == board[i][j] for di, dj in DIRECTION]
    return int(sum(same_block)) == 3

def make_zero_block(four_block, board):
    for i, j in four_block:
        board[i][j] = 0
        for di, dj in DIRECTION:
            board[i + di][j + dj] = 0

def remove_zero_block(m, n, board):
    new_board = []
    for j in range(n):
        stack = []
        for i in range(m):
            if board[i][j]:
                stack.append(board[i][j])
        new_board.append([0 for _ in range(m - len(stack))] + stack)
    
    for i, board_unit in enumerate(zip(*new_board)):
        board[i] = list(board_unit)

def solution(m, n, board):
    board = list(map(list, board))
    
    while True:
        four_block = get_four_block(m, n, board)
        if not four_block:
            break
        make_zero_block(four_block, board)
        remove_zero_block(m, n, board)

    return sum([board_unit.count(0) for board_unit in board])