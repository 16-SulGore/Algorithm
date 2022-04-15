from itertools import combinations

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

def count_set_menu(set_menu_counter, set_menu_order, course):
    if set_menu_counter[course].get(set_menu_order, 0):
        set_menu_counter[course][set_menu_order] += 1
    else:
        set_menu_counter[course][set_menu_order] = 1

def solution(orders, course):
    set_menu_counter = {}
    for now_course in course:
        set_menu_counter[now_course] = {}
        for order in orders:
            for set_menu in combinations(order, now_course):
                set_menu_order = ''.join(sorted(set_menu))
                count_set_menu(set_menu_counter, set_menu_order, now_course)
    return decide_set_menu(set_menu_counter)
            


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

# print(230 & 160 & 162)
print(solution(orders, course))
