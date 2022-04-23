def solution(msg):
    start = end = 0
    msg_length = len(msg)
    msg_dict = {chr(65 + i): i + 1 for i in range(26)}

    answer = []
    while start < msg_length:
        while end < msg_length and msg_dict.get(msg[start:end + 1], 0):
            end += 1
        answer.append(msg_dict[msg[start:end]])
        new_word = msg[start:end + 1]
        msg_dict[new_word] = len(msg_dict) + 1
        start = end
    return answer