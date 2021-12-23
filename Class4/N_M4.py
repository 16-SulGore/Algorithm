def dfs(num):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(num, N + 1):
        arr.append(i)
        dfs(i)
        arr.pop()       

N, M = map(int, input().split())
arr = []

dfs(1)