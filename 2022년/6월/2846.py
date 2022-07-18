n =int(input())
h = list(map(int,input().split()))

result = []
dist = 0
for i in range(n-1):
    if h[i] < h[i+1]:
        dist += h[i+1] - h[i]
    else:
        result.append(dist)
        dist = 0
result.append(dist)

print(max(result))