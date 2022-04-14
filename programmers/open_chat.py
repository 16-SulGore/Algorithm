def solution(record):
    answer = []
    db = {}
    for r in record:
        data = r.split()
        if len(data) == 3:
            db[data[1]] = data[2]
        
    for k in record:
        data = k.split()
        if data[0] == 'Enter':
            answer.append(db[data[1]] + '님이 들어왔습니다.')
        elif data[0] == 'Leave':
            answer.append(db[data[1]] + '님이 나갔습니다.')
    return answer