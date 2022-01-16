# 신규 아이디 추천
import re

def level1(id):
    return id.lower()

def level2(id):
    regex = '([a-zA-Z0-9]|[._-])'
    return ''.join(re.compile(regex, re.I).findall(id))

def level3(id):
    end_len, new_len = -1, len(id)
    
    while end_len != new_len:
        end_len = new_len
        id = id.replace('..', '.')
        new_len = len(id)
        
    return id

def level4(id):
    return id.strip(".")

def level5(id):
    return "a" if len(id) == 0 else id
    
def level6(id):
    return id[:15].rstrip('.') if len(id) >= 16 else id

def level7(id):
    while len(id) <= 2:
        id += id[-1]
    return id

def solution(new_id):
    return level7(level6(level5(level4(level3(level2(level1(new_id)))))))