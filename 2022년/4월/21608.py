n = int(input())
jari = [[0]*n for _ in range(n)]
dx, dy = [1,0,-1,0],[0,1,0,-1]

def OOB(nx,ny):
    return 0 <= nx < n and 0 <= ny < n

student = []
for i in range(n**2):
    idx, like1, like2, like3, like4 = list(map(int,input().split()))
    student.append([idx, [like1, like2, like3, like4]])

for i in range(n**2):
    now = student[i][0]

    stu_x = stu_y = 0
    max_like = max_empty = -1

    for x in range(n):
        for y in range(n):
            if not jari[x][y]:
                empty_cnt = 0
                like_cnt = 0
                for d in range(4) :
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if OOB(nx,ny): # 범위 내에 있고
                        if jari[nx][ny] in student[i][1]: # 해당 자리 학생이 now가 좋아하는 학생일 경우
                            like_cnt += 1
                        if jari[nx][ny] == 0: #빈 자리일 경우
                            empty_cnt += 1

                # 조건 1 : 좋아하는 친구가 주변에 많을 때 (핵인싸)
                if like_cnt > max_like:
                    # 가까이에 좋아하는 친구들이 앉을 수 있는 경우 count
                    stu_x , stu_y = x, y
                    max_like = like_cnt
                    max_empty = empty_cnt

                # 조건 2: 조건 1의 좋아하는 친구가 주변에 많은 경우가 여러 경우일 때
                if like_cnt == max_like:
                    # 빈 자리 개수를 탐색해서 빈 자리를 더 많이 가지고 있는 좌표에 학생 배치
                    if empty_cnt > max_empty:
                        stu_x, stu_y = x, y
                        max_empty = empty_cnt
    # now 학생 배치
    jari[stu_x][stu_y] = now

student = sorted(student)
# 만족도조사
satisfaction = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if OOB(nx, ny):
                if jari[nx][ny] in student[jari[i][j] - 1][1]:
                    cnt += 1
        # 만족도 계산은 10의 0승부터 cnt-1승 까지
        if cnt >= 1:
            satisfaction += 10 ** (cnt - 1)

print(satisfaction)


