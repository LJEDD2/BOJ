game = [[0]*19 for _ in range(19)]
dx, dy = [1, 1, 0, -1], [0, 1, 1, 1]

def OOB(x,y):
    return 0 <= x < 19 and 0 <= y < 19

def Recursive(x,y,d_x,d_y,color):
    if OOB(x,y) and game[x][y] == color:
        return Recursive(x + d_x, y + d_y , d_x , d_y , color) + 1
    return 0

def check(cx,cy,color):
    for d_x,d_y in zip(dx,dy):
        cnt = Recursive(cx + d_x , cy + d_y, d_x , d_y ,color)
        cnt += Recursive(cx - d_x , cy - d_y, -d_x , -d_y ,color)
        if cnt + 1 == 5:
            return True
    return False

for k in range(1,int(input())+1):
    x,y = map(int,input().split())
    if check(x-1,y-1,k%2+1):
        print(k)
        exit()
    game[x-1][y-1] = k % 2 + 1

print(-1)
