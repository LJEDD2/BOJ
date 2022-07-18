n,m = map(int,input().split())
n_ = set([input() for _ in range(n)])
m_ = [input() for _ in range(m)]

cnt = 0
for i in m_:
    if i in n_:
        cnt += 1
print(cnt)