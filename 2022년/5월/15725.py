s = input().split('x')
if len(s) == 1:
    print(0)
else:
    if s[0] == '':
        print(1)
    elif s[0] == '-':
        print(-1)
    else:
        print(s[0])
