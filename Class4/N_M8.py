N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []

def dfs(num):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(num, N):
        result.append(arr[i])
        dfs(i)
        result.pop()         
        
dfs(0)