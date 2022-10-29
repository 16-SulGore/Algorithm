# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10

    disks = []
    for disk in stack1:
        disks.append(['1',disk])
    for disk in stack2:
        disks.append(['2',disk])
    for disk in stack3:
        disks.append(['3',disk])

    disks.sort(key= lambda x: x[1])
    result = ''
    for s in disks[::-1]:
        result += s[0]
    return result

print(solution([2,7],[4,5],[1]))