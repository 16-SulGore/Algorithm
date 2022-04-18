def get_sets(s):
    sets = []
    for char in s.split('},{'):
        now_sets = set()
        for c in char.split(','):
            now_sets.add(int(c))
        sets.append(now_sets)
    return sorted(sets, key=lambda x: len(x))

def solution(s):
    answer = []
    sets = [set()] + get_sets(s[2:-2])
    for i in range(len(sets) - 1):
        answer.append((sets[i + 1] - sets[i]).pop())
    return answer