# 9465 스티커 [실버 1]
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    sticker = [list(map(int, input().split())), list(map(int, input().split()))]
    
    dp = [[0, 0] for _ in range(len(sticker[0]) + 2)]
    for i in range(N):
        dp[i + 2][1] = sticker[1][i] + max(dp[i + 1][0], max(dp[i]))
        dp[i + 2][0] = sticker[0][i] + max(dp[i + 1][1], max(dp[i]))

    print(max(dp[-1]))