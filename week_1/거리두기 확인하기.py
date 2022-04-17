def check_room(room):
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    for y, line in enumerate(room):
        for x in range(len(line)):
            seat = line[x]
            if not (seat == 'P' or seat == 'O'):
                continue
            
            person = 0
            for dx, dy in direction:
                px, py = x + dx, y + dy
                if not 0 <= px < len(line):
                    continue
                if not 0 <= py < len(room):
                    continue
                
                side_seat = room[py][px]
                if side_seat == 'P':
                    person += 1
            
            if seat == 'P' and person >= 1:
                return False
            if seat == 'O' and person >= 2:
                return False
    
    return True

def solution(places):
    result = [True] * len(places)
    
    for i, room in enumerate(places):
        result[i] = int(check_room(room))
            
    return result