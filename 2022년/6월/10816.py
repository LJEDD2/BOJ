n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

cnt = {}
for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

result = []
for j in m_list:
    if j in cnt:
        result.append(cnt[j])
    else:
        result.append(0)
print(*result)