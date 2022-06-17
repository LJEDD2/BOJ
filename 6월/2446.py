n = int(input())
a = 2*n-1
for i in range(n):
    print(' '*i+'*'*(a-2*i))
for i in range(n-2,-1,-1):
    print(' '*i+'*'*(a-2*i))

