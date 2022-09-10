# Ex_16566 카드게임 [플5]
# upper bound
def upperBound(target):
    s, e = 0, M

    while s < e:
        mid = (s + e) // 2
        if cards[mid] <= target:
            s = mid + 1
        else:
            e = mid
    return e


def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
    return graph[x]


def union(child, parent):
    if parent < M:
        graph[find(child)] = find(parent)


N, M, K = map(int, input().split())
cards = sorted(map(int, input().split()))
cCards = list(map(int, input().split()))
graph = list(i for i in range(M))

for cCard in cCards:
    index = find(upperBound(cCard))
    print(cards[index])

    union(index, index + 1)
