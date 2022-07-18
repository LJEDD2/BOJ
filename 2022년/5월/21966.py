n = int(input())
s = list(input())

if n <= 25:
    print(*s,sep="")
else:
    if '.' not in s[11:-12]:
        print(*s[:11],"...",*s[-11:],sep="")
    else:
        print(*s[:9],"......",*s[-10:],sep="")
