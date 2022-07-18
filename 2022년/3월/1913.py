def drwaing_graph(n,m):
    arr = [[0] * n for _ in range(n)]
    idx = x = y = 0
    dx , dy = [1,0,-1,0], [0,1,0,-1] # 아래, 오른쪽, 위쪽, 왼쪽 순서
    arr[x][y] = n**2
    num = n**2 - 1
    # 좌표는 1,1 부터 카운트
    ans_x, ans_y = 1, 1

    while num > 0:
        move_x , move_y = x + dx[idx], y + dy[idx]
        if 0 <= move_x < n and 0 <= move_y < n and arr[move_x][move_y] == 0:
            # target 만나면 좌표 저장해주기

            arr[move_x][move_y] = num
            if arr[move_x][move_y] == m:
                ans_x, ans_y = move_x+1, move_y+1
            x, y = move_x, move_y
            num -= 1

        else:
            #방향
            idx = (idx+1) % 4
    return arr, ans_x, ans_y

n = int(input())
m = int(input())
graph , ans_x, ans_y = drwaing_graph(n,m)

for i in graph:
    print(*i)
print(ans_x, ans_y)





