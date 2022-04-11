from enum import Enum
from collections import deque

class OrderType(Enum):
    Enter = "님이 들어왔습니다."
    Leave = "님이 나갔습니다."
    Change = ""

class User:
    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname
        self.records = deque([OrderType.Enter])

    def enter(self, new_nickname):
        self.nickname = new_nickname
        self.records.append(OrderType.Enter)

    def change(self, new_nickname):
        self.nickname = new_nickname

    def leave(self):
        self.records.append(OrderType.Leave)

    def popleft_record(self):
        return self.nickname + self.records.popleft().value

def solution(record):

    def parse(record_unit):
        records = record_unit.split()

        if len(records) == 2:
            order, user_id = records
        elif len(records) == 3:
            order, user_id, nickname = records

        if order == OrderType.Enter.name:
            if user_id in user_table:
                user_table[user_id].enter(nickname)
            else:
                user_table[user_id] = User(user_id, nickname)

            answer_list.append(user_id)

        elif order == OrderType.Leave.name:
            user_table[user_id].leave()
            answer_list.append(user_id)

        elif order == OrderType.Change.name:
            user_table[user_id].change(nickname)

    user_table = {}
    answer_list = []
    for record_unit in record:
        parse(record_unit)

    return [user_table[user_id].popleft_record() for user_id in answer_list]