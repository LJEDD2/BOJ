s = input()
sumv = 10
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        sumv += 10
    else:
        sumv += 5
print(sumv)
