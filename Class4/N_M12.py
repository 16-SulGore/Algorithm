def dfs(num):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(num, len(arr)):
        result.append(arr[i])
        dfs(i)
        result.pop() 
        
N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
result = []
                
dfs(0)