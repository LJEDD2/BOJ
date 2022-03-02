import sys
s, t = sys.stdin.readline().rstrip(),sys.stdin.readline().rstrip()
while True:
    # 맨 뒤 값이 A인지 B인지 따져보고 뒤집기
    # 맨뒤에꺼 빼주고 뒤집어줘야함
    if t[-1] == 'A':
        #A일때는
        t = t[::-1]
    else:
        t = t[:-1][::-1]

    # 크기가 같아지고 while 탈출
    if len(s) == len(t):
        break

if s == t:
    print(1)
else:
    print(0)



