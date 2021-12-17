n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))


for m_num in m_list:
    
    print("1") if m_num in n_list else print("0")
