a, b = map(int,input().split())
monster  = a - ((a*b/100))

if monster >= 100:
    print(0)
else:
    print(1)
