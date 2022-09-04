# Ex_1043 거짓말 골4
import sys
from collections import deque

def input_list() -> list:
    return list(map(int, sys.stdin.readline().split()))


N, M = map(int, input().split())
smartors = input_list()[1:]

# set visitor, party
visitors_parties = [[] for _ in range(N + 1)]
parties = [[] for _ in range(M)]
for party_num in range(M):
    visitors = input_list()[1:]

    # visitor의 소속 파티
    for visitor in visitors:
        visitors_parties[visitor].append(party_num)

    # party의 참가 인원
    parties[party_num] = visitors

# bfs
fake_parties = [True] * M
visited = [False] * (N + 1)
dq = deque(smartors)

while dq:
    visitor = dq.popleft()
    if not visited[visitor]:
        visited[visitor] = True

        for party_num in visitors_parties[visitor]:
            fake_parties[party_num] = False

            for duplicated_visitor in parties[party_num]:
                dq.append(duplicated_visitor)


print(sum(fake_parties))
