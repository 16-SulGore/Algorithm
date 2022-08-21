import sys
input = sys.stdin.readline
N = 9

def is_unique(x, y, target):
    global graph, N
    for i in range(N):
        if graph[y][i] == target or graph[i][x] == target:
            return False
    
    squared_x = x // 3 * 3
    squared_y = y // 3 * 3
    for a in range(squared_x, squared_x + 3):
        for b in range(squared_y, squared_y + 3):
            if graph[b][a] == target:
                return False
    
    return True

def backtrack(num):
    global graph, N
    if num == N * N:
        for i in range(N):
            print(''.join(map(str, graph[i])))
        exit(0)
    
    x = num % N
    y = num // N
    if graph[y][x] != 0:
        return backtrack(num + 1)
    
    for i in range(1, N + 1):
        if is_unique(x, y, i):
            graph[y][x] = i
            backtrack(num + 1)
            graph[y][x] = 0

graph = [list(map(int, input().strip())) for _ in range(N)]
backtrack(0)
