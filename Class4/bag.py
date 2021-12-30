import sys
input = sys.stdin.readline

def dfs(num, bag, value):
    global result
    result = max(value, result)

    for i in range(num, N):
        w, v = things[i]
        if K >= bag + w:
            dfs(i, bag + w, value + v)

N, K = map(int, input().split())

things = []
for _ in range(N):
    weight, value = map(int, input().split())
    things.append([weight, value])

result = 0
dfs(num = 0, bag = 0, value = 0)

print(result)