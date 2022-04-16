dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
ROW, COL = 5, 5


def solution(places):
    return [int(is_good(place)) for place in places]

def is_good(place):
    stack = [[x, y] for x in range(ROW) for y in range(COL) if place[x][y] == "P"]
    visited = [[False for __ in range(ROW)] for _ in range(COL)]
    can_go = lambda x, y: 0 <= x < COL and 0 <= y < ROW and place[x][y] != "X"

    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            if not visited[x][y]:
                visited[x][y] = True
                nx, ny = x + dx[i], y + dy[i]
                
                if can_go(nx, ny):
                    if place[nx][ny] == "P":
                        return False 
                    elif place[nx][ny] == "O" and place[x][y] == "P":
                        stack.append([nx, ny])
    return True