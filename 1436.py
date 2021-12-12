import math

N = int(input())

count_n = 0
prefix = 0

while count_n != N :

    count_n += 1

    num = [6,6,6] # 시작 666
    a = list(str(prefix)) # 카운트
    
    # num 앞에 a를 더함 1,6,6,6 -> 2,6,6,6 - ... -> 1,0,6,6,6 // a[1,0]
    num = list(map(int, a)) + num

    count_six = 0
    for j in range(len(num)) : # 앞에서 부터 6의 개수를 셈

        if count_six == 3 :
            for h in range(j,len(num)):
                num[h] = 0
            # count_n + 접미어로 붙일 수 있는 숫자의 개수 
            len_place_value = len(num) - j
            if N > count_n + math.pow(10, len_place_value ) - 1 : 
                count_n += int(math.pow(10, len_place_value) - 1)
            else :
                alpha_num = N - count_n
                for h in range(len_place_value):
                    num[-(h+1)] = int(alpha_num % 10)
                    alpha_num /= 10
                count_n = N
            break

        count_six = 1 + count_six if num[j]==6 else 0                
        
    prefix += 1

result = "".join(map(str, num))
print(result.lstrip("0"))
        
       