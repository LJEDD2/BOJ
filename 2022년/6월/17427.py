sumv = 0
n = int(input())
for i in range(1,n+1):
    sumv += (n // i) * i
print(sumv)
