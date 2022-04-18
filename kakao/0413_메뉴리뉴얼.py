ALPHA_COUNT = ord('Z') - ord('A')

def solution(orders, course):
    dp, menu_count = get_dp(orders)

    result = []
    for course_count in course:
        result += get_menu_course(dp, course_count, menu_count)
    
    return sorted(result)

def get_dp(orders):
    dp = [[] for _ in range(ALPHA_COUNT + 1)]
    count = [0 for _ in range(ALPHA_COUNT + 1)]

    for order in orders:
        end = order[0]
        for char in order[1:]:
            if char not in dp[ord(end) - ord('A')]:
                dp[ord(end) - ord('A')] += char

            count[ord(end) - ord('A')] += 1
            end = char

    return dp, count

def get_menu_course(dp, course_count, menu_count):
    stack = []
    for i in range(ALPHA_COUNT + 1):
        if dp[i]:
            stack.append(["", i])

    # dfs
    result = []
    while stack:
        node, index = stack.pop()
        char = chr(index + ord('A'))
        if can_visit(menu_count, char, node):
            node += char

        if len(node) == course_count:
            result.append(node)
        
        else:
            for char in dp[index]:
                if can_visit(menu_count, char, node):
                    stack.append([node + char, index])
    
    return result

def can_visit(menu_count, char, node):
    return char not in node and menu_count[ord(char) - ord('A')] >= 2

###
# answer
def printAnswer():
    a = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    b = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
    c = solution(["XYZ", "XWY", "WXA"], [2,3,4])
    
    print("a", a == ["AC", "ACDE", "BCFG", "CDE"], a)
    print("b", b == ["ACD", "AD", "ADE", "CD", "XYZ"], b)
    print("c", c == ["WX", "XY"], c)

printAnswer()