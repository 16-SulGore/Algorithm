n = int(input())
comp_list = [0]
count_num = 0
result_list = []
is_error = False

input_list = [int(input()) for _ in range(n)]

for i in range(n) :

    while input_list[i] != comp_list[-1] :

        if input_list[i] > comp_list[-1] :
            comp_list.append(count_num)
            comp_list[-1] += 1
            count_num = max(count_num, comp_list[-1])
            result_list.append("+")     
        
        elif input_list[i] < comp_list[-1]:
            is_error = True
            break

    if is_error:
        break

    comp_list.pop()
    result_list.append("-")

if is_error == True :
    print("NO")

else :
    for i in result_list:
        print(i)