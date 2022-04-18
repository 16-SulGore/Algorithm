from itertools import combinations

def power_set(size):
    return [format(i, 'b').zfill(size) for i in range(1, 2 ** size)]

def order_to_int(order, order_alpha):
    return int(''.join([str(int(now_alpha in order)) for now_alpha in order_alpha]), 2)

def decide_set_menu(set_menu_counter):
    set_menu = []
    for now_course in set_menu_counter.keys():
        sorted_menu = sorted(set_menu_counter[now_course].items(), key=lambda x: -x[1])
        max_cnt = 0 if not sorted_menu or sorted_menu[0][1] == 1 else sorted_menu[0][1]
        for menu, cnt in sorted_menu:
            if cnt != max_cnt:
                break
            set_menu.append(menu)
    return sorted(set_menu)

def set_menu_in_order(set_menu, order):
    return set_menu & order == set_menu

def count_set_menu(set_menu_counter, set_menu_order, course):
    if set_menu_counter[course].get(set_menu_order, 0):
        set_menu_counter[course][set_menu_order] += 1
    else:
        set_menu_counter[course][set_menu_order] = 1

def solution(orders, course):
    order_alphas = sorted(set(''.join(orders)))
    order_int = [order_to_int(order, order_alphas) for order in orders]

    set_menu_counter = {}
    for now_course in course:
        set_menu_counter[now_course] = {}
        for set_menu in combinations(order_alphas, now_course):
            for order in order_int:
                set_menu_int = order_to_int(set_menu, order_alphas)
                if set_menu_in_order(set_menu_int, order):
                    set_menu_order = ''.join(set_menu)
                    count_set_menu(set_menu_counter, set_menu_order, now_course)
    return decide_set_menu(set_menu_counter)
