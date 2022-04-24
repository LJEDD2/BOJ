board = [list(map(str,input().split())) for _ in range(5)]
dx, dy = [1,0,-1,0],[0,1,0,-1]

def OOB(x,y):
    return 0 <= x < 5 and 0 <= y < 5

def dfs(x,y,word):
    word += board[x][y]

    if len(word) == 6:
        result.append(word)
        return

    for d_x,d_y in zip(dx,dy):
        nx = x + d_x
        ny = y + d_y
        if OOB(nx,ny):
            dfs(nx,ny,word)

result = []
for i in range(5):
    for j in range(5):
        if board[i][j]:
            dfs(i,j,'')

print(len(set(result)))
