answer = []

while True :
    num = input()
    if num == "0" : 
        break

    reverse_num = num[::-1]

    if num == reverse_num : 
        answer.append("yes")
    else :
         answer.append("no")

for i in answer : 
    print(i)
