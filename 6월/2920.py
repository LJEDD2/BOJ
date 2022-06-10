n = list(map(int,input().split()))
if n == sorted(n):
    print("ascending")
elif n == sorted(n,reverse=True):
    print("descending")
else:
    print("mixed")
