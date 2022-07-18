a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
d = {}
for i in range(26):
    d[k[i]] = a[i]

s = input()
for i in s:
    print(d[i] , end="")
