# 가장 긴 증가하는 부분 수열 5

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

def appendSpot():
    for element in elements[1:]:
        if element > dp[-1]:
            dp.append(element)
            spotList.append(len(dp))
        else:
            spot = findSpot(element)

            dp[spot] = element
            spotList.append(spot + 1)
        
def matchSpot():
    result, resultIndex = [], len(dp)
    for i in range(1, N + 1):
        if resultIndex < 0:
            break

        if spotList[-i] == resultIndex:
            resultIndex -= 1
            result.append(elements[-i])

    return result[::-1]
    
N = int(input())
elements = list(map(int, input().split()))

dp = [elements[0]]
spotList = [1]
appendSpot()

print(len(dp))
print(*matchSpot())
