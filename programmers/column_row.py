# 카카오 기출 기둥과 보

def valid(wall, x,y,a):
    # 보 확인
    if a:
        if wall[y-1][x][0] == 0 or wall[y-1][x+1][0] == 0:
            return True
        elif wall[y][x-1][1] == 1 and wall[y][x+1][1] == 1:
            return True
    # 기둥 확인
    else:
        if y == 0:
            return True
        elif wall[y][x-1][1] == 1 or wall[y][x][1] == 1:
            return True
        elif wall[y-1][x][0] == 0:
            return True
    return False


def solution(n, build_frame):
    answer = []
    wall = [[[-1, -1] for _ in range(n+1)]for _ in range(n+1)]

    for x, y, a, b in build_frame:
        if b:
            if valid(wall,x,y,a):
                wall[y][x][a] = a
                answer.append([x,y,a])
        else:
            wall[y][x][a] = -1
            answer.remove([x,y,a])
            for x1, y1, a1 in answer:
                if not valid(wall, x1, y1, a1):
                    answer.append([x,y,a])
                    wall[y][x][a] = a
                    break
    return sorted(answer)