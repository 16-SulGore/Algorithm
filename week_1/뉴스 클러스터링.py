def string_to_counted(string):
    result = dict()
    for i in range(len(string) - 1):
        target = string[i:i + 2].lower()
        if not target.isalpha():
            continue
        if not target in result:
            result[target] = 0
        result[target] += 1
    return result

def division(a, b):
    if b == 0:
        return 1
    return a / b

def solution(str1, str2):
    words_count1 = string_to_counted(str1)
    words_count2 = string_to_counted(str2)
    union_set = set(words_count1.keys()) | set(words_count2.keys())
    
    intersection_count = 0
    union_count = 0
    for word in union_set:
        a = words_count1[word] if word in words_count1 else 0
        b = words_count2[word] if word in words_count2 else 0
        intersection_count += min(a, b)
        union_count += max(a, b)
    
    return int(division(intersection_count, union_count) * 65536)