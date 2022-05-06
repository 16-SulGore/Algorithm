# Key 와 Lock을 비교할 때 수월하기 위해 Lock을 변경
# 1. Lock의 길이를 확장, 0과 1을 반대로 변환
# 2. Lock의 홈 개수 확인
def induce_lock(lock, m):
    n = len(lock)
    ext = n + 2 * (m - 1)
    count = 0
    converted = [[False] * ext for _ in range(ext)]
    for y in range(n):
        for x in range(n):
            count += not lock[y][x]
            converted[y + (m - 1)][x + (m - 1)] = not lock[y][x]
    
    return (converted, count)

def rotate_90_graph(graph):
    l = len(graph)
    result = [[False] * l for _ in range(l)]
    
    for y in range(l):
        for x in range(l):
            result[y][x] = bool(graph[l - 1 - x][y])
    
    return result

# 중앙 Lock 부분만을 비교
def derive_key(key, induced, standard, count):
    m, n = len(key), len(induced) - (2 * (len(key) - 1))
    bx, by = standard
    gap = m - 1
    sx, sy = max(bx, gap), max(by, gap)
    ex, ey = min(bx + m, gap + n), min(by + m, gap + n)

    for y in range(sy, ey):
        for x in range(sx, ex):
            key_v, lock_v = key[y - by][x - bx], induced[y][x]
            count -= key_v and lock_v
            if key_v ^ lock_v:
                return False
    
    return count == 0

def solution(key, lock):
    m, n = len(key), len(lock)
    induced, count = induce_lock(lock, m)
    
    comp_l = n + (m - 1)
    for _ in range(4):
        key = rotate_90_graph(key)
        for y in range(comp_l):
            for x in range(comp_l):
                if derive_key(key, induced, (x, y), count):
                    return True

    return False