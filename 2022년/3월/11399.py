n = int(input())
p = sorted(list(map(int, input().split())))

for i in range(1,n):
    p[i] = p[i] + p[i-1]

print(sum(p))