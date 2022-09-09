# Ex_1208 부분수열의 합 2 [골1]

def getSubset(length, start):
    target = [0] * (1 << length)
    for i in range(1 << length):
        for j in range(length):
            if (i & (1 << j)) > 0:
                target[i] += nList[start + j]

    return target


N, S = map(int, input().split())
nList = list(map(int, input().split()))
answer = 0

a = N // 2
b = N - a

left = sorted(getSubset(a, 0))
right = sorted(getSubset(b, a), reverse=True)

i, j = 0, 0
while i < (1 << a) and j < (1 << b):

    if left[i] + right[j] == S:
        left_stack, right_stack = 1, 1

        while i < ((1 << a) - 1) and left[i] == left[i + 1]:
            left_stack += 1
            i += 1

        while j < ((1 << b) - 1) and right[j] == right[j + 1]:
            right_stack += 1
            j += 1

        answer += left_stack * right_stack
        i, j = i + 1, j + 1

    elif left[i] + right[j] < S:
        i += 1

    else:
        j += 1

print(answer if S != 0 else answer - 1)
