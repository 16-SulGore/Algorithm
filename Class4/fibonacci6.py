from collections import deque

n = int(input())

dp = deque([0])
dp.append(1)

for i in range(2, n + 1):
    dp.append(dp[0]+ dp[1])
    dp.popleft()
print(dp[1]%1000000007)