N = int(input())
values = list(map(int, input().split()))

start, end = 0, len(values) - 1
answer = [values[-2], values[-1]]
while start < end:
    sumValues = values[start] + values[end]
    
    if abs(sum(answer)) > abs(sumValues):
        answer = [values[start], values[end]]
    
    if sumValues > 0:
        end -= 1
    elif sumValues < 0:
        start += 1
    else:
        break
    
print(*answer)
