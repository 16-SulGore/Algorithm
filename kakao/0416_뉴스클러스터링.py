def solution(str1, str2):
    set1, set2 = get_set(str1), get_set(str2)
    similarity = get_jaccard(set1, set2)
    
    return int(similarity * 65536)

def get_set(str):
    set = []
    
    end = str[0].upper()
    for char in str[1:]:
        if char.isalpha() and end.isalpha():
            set.append(end + char.upper())
        end = char.upper()
    
    return set

def get_jaccard(set1, set2):
    if len(set1) == 0 and len(set2) == 0:
        return 1

    intersection_count = get_intersection_count(set1, set2)
    total_count = len(set1) + len(set2) - intersection_count

    return intersection_count / total_count 

def get_intersection_count(set1, set2):
    intersection_count = 0
    visited_set1 = [False for _ in range(len(set1))]
    visited_set2 = [False for _ in range(len(set2))]

    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i] == set2[j] and not visited_set1[i] and not visited_set2[j]:
                intersection_count += 1
                visited_set1[i] = True
                visited_set2[j] = True
                break
    
    return intersection_count
