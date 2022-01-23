# 실패율
def fail_percent(score, x):
    return 0 if score[x - 1][1] == 0 else score[x - 1][0] / score[x - 1][1]

def count_score(N, stages):
    # 실패, 성공
    score = [[0, 0] for _ in range(N + 1)]
    
    for stage in stages:
        # 성공 카운팅
        for n in range(stage):
            score[n][1] += 1
            
        # 실패 카운팅
        score[stage - 1][0] += 1
    return score

def solution(N, stages):
    result = [i + 1 for i in range(N)]
    score = count_score(N, stages)
    
    sorted_key = lambda x: (-fail_percent(score, x), x)
    return sorted(result, key = sorted_key)