from collections import deque

n = int(input())
board =[list(input()) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
result = []

def OOB(x,y):
    return 0 <= x < n and 0 <= y < n

def BFS(x,y):
    queue = deque([(x,y)])
    area = 1
    board[x][y] = '0'
    while queue:
        x, y = queue.popleft()
        for d_x, d_y in zip(dx,dy):
            nx = x + d_x
            ny = y + d_y
            if OOB(nx,ny) and board[nx][ny] == '1':
                board[nx][ny] = '0'
                queue.append((nx,ny))
                area += 1
    result.append(area)

for x in range(n):
    for y in range(n):
        if board[x][y] == "1":
            BFS(x,y)

print(len(result))
print(*sorted(result), sep='\n')
