# Ex_1043 거짓말 골4
import sys

def input_list() -> list:
    return list(map(int, sys.stdin.readline().split()))

def set_info(party_info, party_num):
    visitors = party_info[1:]

    # visitor의 소속 파티
    for visitor in visitors:
        visitors_parties[visitor].append(party_num)

    # party의 참가 인원
    parties[party_num] = visitors

# 진실을 말해야하는 인원의 파티를 모두 real 파티로 변환
def set_real_party(visitor):
    for party_num in visitors_parties[visitor]:
        if fake_parties[party_num]:
            fake_parties[party_num] = False
            set_real_visitor(party_num)

# 해당 파티 파티원들을 진실을 말해야되는 인원으로 변환
def set_real_visitor(party_num):
    for visitor in parties[party_num]:
        if not real_visitor[visitor]:
            real_visitor[visitor] = True
            set_real_party(visitor)


N, M = map(int, input().split())
smartors = input_list()[1:]

visitors_parties = [[] for _ in range(N + 1)]
parties = [[] for _ in range(M)]
for party_num in range(M):
    set_info(input_list(), party_num)

fake_parties = [True] * M
real_visitor = [False] * (N + 1)
for smartor in smartors:
    set_real_party(smartor)
    
print(sum(fake_parties))
