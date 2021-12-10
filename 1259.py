answer = []
num = input()

while num != "0" :

    reverse_num = num[::-1]

    if num == reverse_num : 
        answer.append("yes")
    else :
         answer.append("no")
            
    num = input()

for i in answer : 
    print(i)
