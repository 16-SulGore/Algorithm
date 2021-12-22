import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def backtrack(seq, last):
  global N, M
  if len(seq) == M:
    return print(' '.join(map(str, seq)))
  
  for i in range(last, N + 1):
    backtrack(seq + [i], i)

backtrack([], 1)