def func(f):
    global n_list,n
    flag = False
    start , end = 0,0

    for i in f:
        if i == 'R':
            flag = not flag
        else:
            if n == 0:
                return 'error'
            n -= 1
            if flag:
                end += 1
            else:
                start += 1
    else:
        if flag:
            n_list.reverse()
            if start == 0:
                return n_list[end:]
            return n_list[end:-start]
        else:
            if end == 0:
                return n_list[start:]
            else:
                return n_list[start:-end]



for _ in range(int(input())):
    f = input().replace('RR','')
    n = int(input())
    if n == 0:
        n_list = input()
        if 'D' in f:
            print('error')
            continue
        else:
            print("[]")
            continue
    n_list = list(input()[1:-1].split(','))
    ans = func(f)

    if ans != 'error':
        print('['+','.join(ans)+']')
    else:
        print(ans)

