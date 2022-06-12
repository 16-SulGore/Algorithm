import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    solutions = sorted(list(map(int, input().split())))

    answer = []
    minValue = float('inf')
    for start in range(n - 2):
        mid, end = start + 1, n - 1
        sumValue = solutions[start]
        while mid < end:
            value = sumValue + solutions[mid] + solutions[end]
            if minValue > abs(value):
                minValue = abs(value)
                answer = [solutions[start], solutions[mid], solutions[end]]
            if value > 0:
                end -= 1
            elif value == 0:
                break
            else:
                mid += 1
    print(*answer)