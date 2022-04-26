def has_score(real_m, music):
    len_m, len_score = len(real_m), len(music)
    for i in range(len_score - len_m + 1):
        if music[i:i+len_m] == real_m:
            return True
    return False

def get_real_score(score):
    real_score = []
    for score_unit in score.split('#'):
        if score_unit:
            real_score += score_unit
            real_score[-1] = score_unit[-1] + '#'
    if score[-1] != '#':
        real_score[-1] = real_score[-1][0]
    return real_score

def get_radio_time(start, end):
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    return (end_h - start_h) * 60 + end_m - start_m

def play_music(radio_time, real_score):
    music_time = len(real_score)
    if music_time <= radio_time:
        music_score = real_score * (radio_time // music_time) + real_score * (radio_time % music_time)
    else:
        music_score = real_score[:radio_time]
    return music_score

def solution(m, musicinfos):
    answer = []
    real_m = get_real_score(m)
    for musicinfo in musicinfos:
        start, end, title, score = musicinfo.split(',')
        radio_time, real_score, real_m = get_radio_time(start, end), get_real_score(score), get_real_score(m)
        music = play_music(radio_time, real_score)
        if has_score(real_m, music):
            answer.append((title, radio_time))
    return (answer and sorted(answer, key=lambda x: (-x[1]))[0][0]) or "(None)"