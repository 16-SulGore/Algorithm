def isPromising(x, y, n):
    return not visitedX[x][n] and not visitedY[y][n] and not visitedBox[boxX(x, y)][n]

def visit(x, y, n):
    board[x][y] = n 
    visitedX[x][n] = True
    visitedY[y][n] = True
    visitedBox[boxX(x, y)][n] = True

def back(x, y, n):
    board[x][y] = EMPTY
    visitedX[x][n] = False
    visitedY[y][n] = False
    visitedBox[boxX(x, y)][n] = False
    
def dfs(i):
    if i == lenS:
        for x in range(ROW):
            print(''.join(map(str, board[x])))
        stack.clear()
        return

    if len(stack) == 0 or i > len(stack):
        return

    x, y = stack[i]
    for n in range(1, ROW + 1):
        if isPromising(x, y, n):
            backtrack(x, y, n, i)

def backtrack(x, y, n, i):
    visit(x, y, n)
    dfs(i + 1)
    back(x, y, n)

COL = ROW = 9
EMPTY = 0

board = [[0] * ROW for _ in range(COL)]
visitedX, visitedY, visitedBox = [[[False] * (ROW + 1) for _ in range(COL)] for _ in range(3)]
boxX = lambda x, y: x // 3 + (y // 3) * 3

stack = []
for x in range(COL):
    thisLine = list(map(int, input()))

    for y in range(ROW):
        board[x][y] = thisLine[y]

        if board[x][y] == EMPTY:
            stack.append([x, y])

        else:
            visitedX[x][board[x][y]] = True
            visitedY[y][board[x][y]] = True
            visitedBox[boxX(x, y)][board[x][y]] = True
lenS = len(stack)

dfs(0)
