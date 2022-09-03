from functools import reduce

K, N = map(int, input().split())
lan_list = list(int(input()) for _ in range(K))

start, end = 1, max(lan_list)
while start <= end:
    mid = (start + end) // 2

    if reduce(lambda acc, cur: acc + cur // mid, lan_list, 0) >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
