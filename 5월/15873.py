n = input()
if len(n) >= 3 :
    if int(n[:2]) > 10:
        print(int(n[:1]) + int(n[1:]))
    else:
        print(int(n[:2])+int(n[2:]))
elif len(n) == 2:
    print(int(n[0])+int(n[1]))
else:
    print(int(n))
