from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def waiting_room(room):
    person = []
    for n in range(5):
        for m in range(5):
            if room[n][m] == 'P':
                person.append([n, m, 0])
    return person

def keep_distance(place):
    for person in waiting_room(place):
        people = deque([person])
        visited = [[False for _ in range(5)] for _ in range(5)]
        visited[person[0]][person[1]] = True
        while people:
            x, y, distance = people.popleft()
            for n in range(4):
                nx = dx[n] + x
                ny = dy[n] + y

                if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                    continue
                elif not visited[nx][ny] and distance < 2:
                    if place[nx][ny] == 'P':
                        return False
                    elif place[nx][ny] == 'O':
                        visited[nx][ny] = True
                        people.append([nx, ny, distance + 1])
    return True

def solution(places):
    return [1 if keep_distance(place) else 0 for place in places]