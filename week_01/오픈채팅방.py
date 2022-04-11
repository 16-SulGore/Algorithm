def solution(record):
    response = ['님이 들어왔습니다.', '님이 나갔습니다.']
    my_record = []
    uid = {}
    
    for now_record in record:
        data = now_record.split()
        nowv = [data[1], 0]

        if data[0] == 'Leave': 
            nowv[1] = 1
        else: 
            uid[data[1]] = data[2]

        data[0] != 'Change' and my_record.append(nowv)
    
    result = [uid[now_uid] + response[now_response] for now_uid, now_response in my_record]
    return result