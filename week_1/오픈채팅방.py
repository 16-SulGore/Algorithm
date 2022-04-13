def log_to_string(op, name):
    if op == "Enter":
        return name + "님이 들어왔습니다."
    if op == "Leave":
        return name + "님이 나갔습니다."

def solution(record):
    user_log = []
    user_info = dict()
    for string in record:
        line = string.split(" ")
        op, uid = line[0], line[1]

        if op != "Leave":
            name = line[2]
            user_info[uid] = name
            
        if op != "Change":
            user_log.append((op, uid))

    return [log_to_string(op, user_info[uid]) for op, uid in user_log]