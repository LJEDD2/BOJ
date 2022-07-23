n , k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

for line in board:
    for _ in range(k):
        for l in line:
            print(f'{l} '*k , end="")
        print()