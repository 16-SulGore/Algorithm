# Ex_15652 N과 M(4): 실3
def backtrack(list, min):
    if len(list) == M:
        print(*list)
        return

    for i in range(min, N + 1):
        backtrack(list + [i], i)


N, M = map(int, input().split())

backtrack([], 1)