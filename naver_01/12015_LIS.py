import bisect

if __name__ == "__main__":
    n = int(input())
    array = [0] + list(map(int, input().split()))
    dp = [0]
    for i in range(1, n + 1):
        if dp[-1] < array[i]:
            dp.append(array[i])
        else:
            target_index = bisect.bisect_left(dp, array[i])
            dp[target_index] = array[i]
    print(len(dp) - 1)