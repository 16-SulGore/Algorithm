# 가장 긴 증가하는 부분 수열 2

def findSpot(element):
    start, end = 0, len(dp) - 1

    while start < end:
        mid = (start + end) // 2

        if dp[mid] < element:
            start = mid + 1
        elif dp[mid] == element:
            return mid
        else:
            end = mid 
            
    return end
        
N = int(input())
elements = list(map(int, input().split()))

dp = [elements[0]]

for element in elements:
    if element > dp[-1]:
        dp.append(element)
    else:
        dp[findSpot(element)] = element
    
print(len(dp))