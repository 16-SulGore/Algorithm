if __name__ == "__main__":
    k, n = map(int, input().split())
    start = end = 1
    lan_cables = []

    for _ in range(k):
        lan_cable = int(input())
        lan_cables.append(lan_cable)
        end = max(end, lan_cable)

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for lan_cable in lan_cables:
            cnt += lan_cable // mid

        if cnt >= n:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    
    print(answer)