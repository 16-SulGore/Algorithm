from itertools import combinations

def solution(orders, course):
    chosen = list()
    orders = list(map(sorted, map(list, orders)))
    for num in course:
        # 메뉴 조합의 정보 구하기       
        memory = set()
        order_log = dict()
        for order in orders:
            menus = list(map(''.join, combinations(order, num)))
            for menu in menus:
                if menu in memory:
                    order_log[menu] += 1
                else:
                    order_log[menu] = 1
                    memory.add(menu)
        
        # 구성된 메뉴가 없다면 패스
        if not len(memory):
            continue
        
        # 가장 많이 주문된 수 찾기
        maximum = max(list(order_log.items()), key = lambda x: x[1])[1]
        if maximum < 2:
            continue
        
        # 메뉴 구성 후보 저장
        chosen += list(filter(lambda x: order_log[x] == maximum, order_log.keys()))
        
    return sorted(chosen)