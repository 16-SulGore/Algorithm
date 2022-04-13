from collections import deque

def check_distance(place):
    ROW = COL = 5
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(ROW):
        for j in range(COL):
            if place[i][j] == 'P':
                visited = [[0 for _ in range(ROW)] for _ in range(COL)]

                q = deque([(i, j, 0)])
                while q:
                    now_i, now_j, distance = q.popleft()
                    visited[now_i][now_j] = 1

                    for di, dj in direction:
                        next_i = now_i + di
                        next_j = now_j + dj
                        if 0 <= next_i < ROW and 0 <= next_j < COL:
                            if not visited[next_i][next_j] and distance < 2:
                                if place[next_i][next_j] == 'O':
                                    q.append((next_i, next_j, distance + 1))
                                elif place[next_i][next_j] == 'P':
                                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        answer.append(1 if check_distance(place) else 0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))