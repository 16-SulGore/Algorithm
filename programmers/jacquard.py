# 카카오 기출
def multiple_sets(string):
    list1 = []
    for i in range(len(string) - 1):
        if string[i: i+2].isalpha():
            list1.append(string[i:i+2])
    return list1

def jacquard(x, y):
    if y == 0:
        return 65536
    elif x == 0:
        return 0
    return int(x / y * 65536)
        

def solution(str1, str2):
    list1 = multiple_sets(str1.upper())
    list2 = multiple_sets(str2.upper())
    
    union = list(set(list1)|set(list2))
    gyo = 0
    hap = 0
    
    for data in union:
        a = list1.count(data)
        b = list2.count(data)
        gyo += min(a, b)
        hap += max(a, b)
        
    return jacquard(gyo, hap)