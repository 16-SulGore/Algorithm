# EX_1316 그룹 단어 체커

toAscii = lambda x: ord(x) - ord('a')
answer = 0
for word in (input() for _ in range(int(input()))):
    end = -1
    word_list = [False] * (toAscii('z') + 1)
    for c in word:
        if end != c and word_list[toAscii(c)]:
            answer -= 1
            break
        word_list[toAscii(c)] = True
        end = c
    answer += 1

print(answer)
