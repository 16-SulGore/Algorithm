def binary_search(start, end, result) :
    
    mid = (start + end) // 2
    if num_can_made(mid) >= N and mid > result :
        result = mid

    if start >= end:
        return result

    if num_can_made(mid) >= N :
        return binary_search(mid + 1, end, result)

    else :
        return binary_search(start, mid - 1, result)

def num_can_made(cut_len) :
    num = 0
    for len_wire in len_list :
       num += len_wire // cut_len
    return num

K, N = map(int, input().split())
len_list = []
result = 0

for i in range(K) :
    len_list.append(int(input()))

print(binary_search(1, max(len_list), result))