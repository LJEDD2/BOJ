import re
def func(f):
    global n_list,n
    flag = False
    start , end = 0,0

    for i in f:
        if i == 'R': # 홀수개면 True -> 뒤집기
            flag = not flag
        # D일때
        else:
            # 입력된 게 하나도 없으면 => []의 경우
            if n == 0:
                # error return
                return 'error'
            n -= 1
            # 만약 D일 경우 인덱스 출력 위치가 +=1 되는데
            # 여기서 R일 경우 출력 시 start 위치가 맨 뒤로 바뀜
            if flag: # R일 때
                end += 1 # 끝에서 한칸 앞에서부터 출력
            else:
                start += 1 # 앞에서 한칸 뒤부터 출력
    # return 안 만나고 다 돌았으면
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
    n_list = re.findall('\d+',input())
    ans = func(f)

    if ans != 'error':
        print('['+','.join(ans)+']')
    else:
        print(ans)

