def get_power_set(size):
    return [format(i, 'b').zfill(size) for i in range(2**size)]

def back_tracking(idx, banned_id, bids, uid, user_dict, answer):
    if uid in bids:
        return

    uid and bids.append(uid)
    if idx == len(banned_id):
        answer.add('.'.join(sorted(bids)))
        return
    
    for ban_uid in user_dict[banned_id[idx]]:
        back_tracking(idx + 1, banned_id, bids[::], ban_uid, user_dict, answer)
    
def solution(user_id, banned_id):
    user_dict = {}
    for uid in user_id:
        for power_set in get_power_set(len(uid)):
            key = ''.join([uid[i] if power_set[i] == '1' else '*' for i in range(len(power_set))])
            if not user_dict.get(key, 0):
                user_dict[key] = [uid]
            else:
                user_dict[key].append(uid)
    answer = set()
    back_tracking(0, banned_id, [], None, user_dict, answer)
    return len(answer)