# Ex_1644 소수의 연속합 [골3]
import math
from collections import defaultdict

N = int(input())

primes = []
isPrime = [True] * (N + 1)
sumDict = defaultdict(int)
answer = 0

# set prime bool
for i in range(2, int(math.sqrt(N)) + 1):
    if isPrime[i]:
        j = 2
        while i * j <= N:
            isPrime[i * j] = False
            j += 1

# set prime num
for i in range(2, N + 1):
    if isPrime[i]:
        primes.append(i)

# prefix sum
for i in range(len(primes)):
    sumPrime = primes[i]

    if sumPrime == N:
        answer += 1

    for j in range(i + 1, len(primes)):
        sumPrime += primes[j]

        if sumPrime > N:
            break

        if sumPrime == N:
            answer += 1

print(answer)
