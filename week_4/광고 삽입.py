HOUR = 3600
MINUTE = 60

def string_to_second(string):
    hh, mm, ss = string.split(':')
    return int(hh) * HOUR + int(mm) * MINUTE + int(ss)

def second_to_string(seconds):
    hh = seconds // HOUR
    seconds -= hh * HOUR
    mm = seconds // MINUTE
    seconds -= mm * MINUTE
    return ':'.join(map(lambda x: str(x).zfill(2), [hh, mm, seconds]))

def solution(play_time, adv_time, logs):
    timeline = [0] * (100 * HOUR)
    
    for log in logs:
        start, end = map(string_to_second, log.split('-'))
        timeline[start] += 1
        timeline[end] += -1
    
    adv, end = map(string_to_second, [adv_time, play_time])
    before = timeline[0]
    for i in range(1, end):
        timeline[i] += before
        before = timeline[i]
        timeline[i] += timeline[i - 1]
    
    result = 0
    maximum = timeline[adv]
    for i in range(adv + 1, end):
        total = timeline[i] - timeline[i - adv]
        if total > maximum:
            result = i - adv + 1
            maximum = total
        
    return second_to_string(result)