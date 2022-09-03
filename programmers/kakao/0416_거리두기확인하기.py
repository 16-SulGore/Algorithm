directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
ROW, COL = 5, 5


def solution(places):
    return [int(is_good(place)) for place in places]

def is_good(place):
    stack = [[x, y, []] for x in range(ROW) for y in range(COL) if place[x][y] == "P"]
    can_go = lambda x, y, visited: 0 <= x < COL and 0 <= y < ROW and [x, y] not in visited

    while stack:
        x, y, visited = stack.pop()
        
        for dx, dy in directions:
            visited.append([x, y])
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny, visited):
                if place[nx][ny] == "P": 
                    return False
                elif place[nx][ny] == "O" and place[x][y] == "P":
                    stack.append([nx, ny, visited])
    return True