answer = []
num = input()

while num != "0" :

    reverse_num = num[::-1]

    answer.append("yes" if num == reverse_num else "no")
            
    num = input()

print(*answer)   
