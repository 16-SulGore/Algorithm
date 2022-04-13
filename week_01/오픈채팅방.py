def solution(record):
    response = ('님이 들어왔습니다.', '님이 나갔습니다.')
    my_record = []
    uid = {}
    
    for record_unit in record:
        data = record_unit.split()
        now_record = [data[1], 0]

        if data[0] == 'Leave': 
            now_record[1] = 1
        else: 
            uid[data[1]] = data[2]

        data[0] != 'Change' and my_record.append(now_record)
    
    result = [uid[now_uid] + response[now_response] for now_uid, now_response in my_record]
    return result