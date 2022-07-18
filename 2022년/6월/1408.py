b = list(map(int,input().split(':')))
a = list(map(int,input().split(':')))

time = (a[0]*3600+a[1]*60+a[2]) - (b[0]*3600+b[1]*60+b[2])

h = time//3600%24
if h < 10:
    h = '0' + str(h)
m = time//60%60
if m < 10:
    m = '0' + str(m)
s = time%60
if s < 10:
    s = '0' + str(s)

print('{}:{}:{}'.format(h,m,s))