def solve_10157(r,c,target):
    arr = [[0] * c for _ in range(r)]
    dx , dy = [-1,0,1,0], [0,1,0,-1] # 위, 오른쪽, 아래, 왼쪽 순서
    idx = 0

    cur_r = r-1
    cur_c = 0
    num = 1

    # 좌표값 설정
    if target > r*c:
       print(0)
       exit(0)
    else:
        while True:
            if num == target:
                print(cur_c + 1 , r - cur_r)
                break

            arr[cur_r][cur_c] = num
            move_r, move_c = cur_r + dx[idx], cur_c + dy[idx]

            if 0 <= move_r < r and 0 <= move_c < c and arr[move_r][move_c] == 0:
                cur_r , cur_c = move_r, move_c
                num+=1
            else:
                #방향
                idx = (idx+1) % 4
    #return arr

c,r = map(int,input().split())
target = int(input())
#graph = solve_10157(r,c,target)
solve_10157(r,c,target)
#for i in graph:
    #print(*i)