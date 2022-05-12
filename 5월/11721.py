s = input()
ans = ''
for i in range(1,len(s)//10+1):
    print(s[:10])
    s = s[10:]
print(s)
