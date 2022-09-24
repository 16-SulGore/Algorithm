# Ex_2143 두 배열의 합 [골3]
from collections import defaultdict

T = int(input())

n = int(input())
aList = list(map(int, input().split()))
aSum = defaultdict(int)

m = int(input())
bList = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i, n):
        aSum[sum(aList[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        answer += aSum[T - sum(bList[i: j + 1])]

print(answer)
