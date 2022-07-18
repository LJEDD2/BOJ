import datetime
now, dday = input().split(),input().split()
n_d = datetime.date(int(now[0]), int(now[1]), int(now[2]))
d_d = datetime.date(int(dday[0]), int(dday[1]), int(dday[2]))

D_day = str(n_d - d_d).split()[0]

if int(D_day) > -365243:
    print('D'+D_day)
else:
    print('gg')