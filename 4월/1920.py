n = int(input())
n_list = set(input().split())
m = int(input())
m_list = input().split()

for i in m_list:
    print(1) if i in n_list else print(0)
