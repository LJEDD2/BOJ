def solve(n):
    n_list = sorted([list(map(int, input().split())) for _ in range(n)],key = lambda x : x[0])
    cnt = 1
    cut = n_list[0][1]
    for i in range(1,n):
        if n_list[i][1] < cut:
            cnt += 1
            cut = n_list[i][1]
    print(cnt)

for t in range(int(input())):
    n = int(input())
    solve(n)