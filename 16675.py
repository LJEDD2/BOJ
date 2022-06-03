ml,mr,tl,tr = input().split()

# R 바위
# S 가위
# P 보
# 둘다 같은 경우
if ml == mr and tl == tr:
    if ml == 'S':
        if tl == 'P':
            print('MS')
        if tl == 'S':
            print('?')
        if tl == 'R':
            print('TK')
    elif ml == 'R':
        if tl == 'P':
            print('TK')
        if tl == 'R':
            print('?')
        if tl == 'S':
            print('MS')
    else:
        if tl == 'R':
            print('MS')
        if tl == 'P':
            print('?')
        if tl == 'S':
            print('TK')

# TK만 같고 MS은 서로 다를 경우
elif ml != mr and tl == tr:
    if tl == 'S' and 'R' in [ml,mr]:
        print('MS')
    elif tl == 'P' and 'S' in [ml,mr]:
        print('MS')
    elif tl == 'R' and 'P' in [ml, mr]:
        print('MS')
    else:
        print('?')
# MS만 같고 TK은 서로 다를 경우
elif tl != tr and ml == mr:
    if ml == 'S' and 'R' in [tl,tr]:
        print('TK')
    elif ml == 'P' and 'S' in [tl,tr]:
        print('TK')
    elif ml == 'R' and 'P' in [tl, tr]:
        print('TK')
    else:
        print('?')
else:
    print('?')
