M, N = map(int, input().split())

for i in range(M, N+1):

    is_decimal = True

    if i == 1 or (i % 2 == 0 and i != 2) :
        continue
    
    j = 3

    while (j*j <= i):
        if i % j == 0:
            is_decimal = False
            break
        j += 2
    
    if is_decimal == True:
        print(i)

    # O(n루트n)