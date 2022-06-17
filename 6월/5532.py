L = int(input())
A = int(input())
B = int(input())
a = int(input())
b = int(input())

if A%a == 0:
    n = A//a
else:
    n = A//a +1

if B % b == 0:
    m = B // b
else:
    m = B//b + 1

print(L-max(n,m))
