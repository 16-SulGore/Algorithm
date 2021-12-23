# Ex_15666 N과 M(12) 실2

def dfs(list, num_index):
    if len(list) == M:
        print(*list)
        return
    
    for i in range(num_index, N):
        dfs(list + [num_list[i]], i)

_, M = map(int, input().split())
num_list = sorted(set(map(int, input().split()))) # 입력받은 리스트의 중복 제거 + 정렬
N = len(num_list)

dfs([], 0)