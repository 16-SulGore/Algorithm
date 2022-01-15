# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    id_db = [[0] * len(id_list) for _ in range(len(id_list))]

    # indexing
    id_index = {}
    for i, id in enumerate(id_list):
        id_index[id] = i
        
    # reporting
    for node in set(report):
        reporter, reported = node.split()
        id_db[id_index[reported]][id_index[reporter]] = 1
        
    # calculate reported
    for reported in id_db:
        if sum(reported) >= k:
            for i in range(len(reported)):
                answer[i] += reported[i]
    return answer