import sys
input = sys.stdin.readline

maxDp, minDp = [0, 0, 0], [0, 0, 0]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    maxDp = [max(maxDp[:2]) + a, max(maxDp) + b, max(maxDp[1:]) + c]
    minDp = [min(minDp[:2]) + a, min(minDp) + b, min(minDp[1:]) + c]
    
print(max(maxDp), min(minDp))
