# Ex_15657 N과 M(8)

def dfs(list, num_index):
    if len(list) == M:
        print(*list)
        return
    
    for i in range(num_index, N):
        dfs(list + [num_list[i]], i)

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

dfs([], 0)