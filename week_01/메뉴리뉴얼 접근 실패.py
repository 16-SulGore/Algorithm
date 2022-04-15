def power_set(size):
    return [format(i, 'b').zfill(size) for i in range(1, 2 ** size)]

def orders_to_int(orders, alphas):
    return [int(''.join([str(int(now_alpha in order)) for now_alpha in alphas]), 2) for order in orders]

def int_to_order(order, alphas):
    return ''.join([alphas[i] for i, v in enumerate(format(order, 'b').zfill(len(alphas))) if v == '1'])

def find_set_menu(orders_combination):
    value = orders_combination[0]
    for i in range(len(orders_combination)):
        value = value & orders_combination[i]
    return 0 if not is_power_of_two(value) else value

def is_power_of_two(value):
    return value & (value - 1)

def decide_set_menu(set_menu_counter, course):
    set_menu = []
    for now_course in course:
        sorted_menu = sorted(set_menu_counter[now_course].items(), key=lambda x: -x[1])
        max_cnt = 0 if not sorted_menu else sorted_menu[0][1]
        for menu, cnt in sorted_menu:
            if cnt != max_cnt:
                break
            set_menu.append(menu)
    return sorted(set_menu)

def solution(orders, course):
    order_alphas = sorted(set(''.join(orders)))
    order_integers = orders_to_int(orders, order_alphas)
    orders_len = len(orders)
    
    set_menu_counter = {now_course: {} for now_course in course}
    for now_set in power_set(orders_len):
        if now_set.count('1') == 1:
            continue
        
        orders_combination = [order_integers[i] for i in range(orders_len) if now_set[i] == '1']
        possible_set_menu = find_set_menu(orders_combination)
        if possible_set_menu:
            menu = int_to_order(possible_set_menu, order_alphas)
            course_cnt, orders_cnt = len(menu), len(orders_combination)
            if not set_menu_counter[course_cnt].get(menu, 0):
                set_menu_counter[course_cnt][menu] = orders_cnt
            else:
                set_menu_counter[course_cnt][menu] = max(set_menu_counter[course_cnt][menu], orders_cnt)
    return decide_set_menu(set_menu_counter, course)