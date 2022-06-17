N = int(input())
values = sorted(map(int, input().split()))
sumValues = [values[0], values[1], values[2]]

for start in range(N - 2):
    end = N - 1
    mid = start + 1 

    while mid < end:
        curValues = values[start] + values[mid] + values[end]
        if abs(sum(sumValues)) > abs(curValues):
            sumValues = [values[start], values[mid], values[end]]

        if curValues > 0:
            end -= 1
        elif curValues == 0:
            break
        else:
            mid += 1

print(*sumValues)
