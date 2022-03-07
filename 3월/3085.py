import sys
input = sys.stdin.readline

n = int(input())
candy = [list((input())) for _ in range(n)]
maxv = 0

def check():
    # 가로로 탐색
    global maxv
    for i in range(n):
        w_cnt = h_cnt = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j-1]:
                w_cnt += 1
                # else에 넣으면 인덱스 범위 벗어나게 됨.
                maxv = max(w_cnt, maxv)
            else:
                w_cnt = 1

            # 좌표상으로:? 움직일때마다 j가 계속 바뀌기때문에
            # 그 자리에서 세로축 좌표값을 바꿔줘야 한다.
            # ex) (0,1)일 때 그 자리를 기준으로 좌표를 움직여줘야 한다.
            if candy[j][i] == candy[j-1][i]:
                h_cnt += 1
                maxv = max(h_cnt, maxv)
            else:
                h_cnt = 1

for i in range(n):
    for j in range(n):
        # -1 이 되는 구간이 생겨버림
        # (0,0), (0,1), (1,0) 좌표를 건너뛰는 문제
        if j:
            candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
            check()
            candy[i][j-1], candy[i][j] = candy[i][j], candy[i][j-1]
        if i:
            candy[i][j], candy[i-1][j] = candy[i-1][j], candy[i][j]
            check()
            candy[i-1][j], candy[i][j] = candy[i][j], candy[i-1][j]

print(maxv)
