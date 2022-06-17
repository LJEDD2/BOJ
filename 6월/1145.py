n = sorted(list(map(int,input().split())))
minv = n[0]
while True:
    cnt = 0
    for i in n:
        if minv % i == 0:
            cnt += 1
    if cnt > 2:
        print(minv)
        break
    minv += 1
