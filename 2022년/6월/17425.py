def solve(n):
    sumv = 0
    for i in range(1, n + 1):
        sumv += (n // i) * i
    print(sumv)

for _ in range(int(input())):
    n = int(input())
    solve(n)