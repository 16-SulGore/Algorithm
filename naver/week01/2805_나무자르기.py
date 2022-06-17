N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, 2000000000
while start <= end:
    H = (start + end) // 2
    
    if sum([tree - H for tree in trees if tree > H]) >= M:
        start = H + 1
    else:
        end = H - 1
    
print(end)