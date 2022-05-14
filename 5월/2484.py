def solve():
    n = [0] * 7
    for i in nlist:
        n[i] += 1
    maxv = max(n)

    if maxv == 4:
        result.append(50000 + n.index(maxv) * 5000)
    elif maxv == 3:
        result.append(10000 + n.index(maxv) * 1000)
    elif maxv == 2:
        if n.count(2) == 2:
            result.append(2000 + min(nlist) * 500 + max(nlist) * 500)
        else:
            result.append(1000 + n.index(maxv) * 100)
    else:
        result.append(max(nlist) * 100)


result = []
for i in range(int(input())):
    nlist = list(map(int, input().split()))
    solve()
print(max(result))
