n ,m ,q = map(int, input().split())
# 입력
rank = [[[301,0] for _ in range(m+1)] for _ in range(n+1)] # 정답 시간과 오답 패널티를 저장할 배열
for _ in range(q):
    time , team, Id, result = input().split()
    time = int(time)
    team = int(team)
    Id = int(Id)

    # 처음 해결한 문제만 점수 인정
    if rank[team][Id][0] == 301:
        if result == "AC":
            rank[team][Id][0] = time
        else:
            rank[team][Id][1] += 20

grade = [[i,0,0] for i in range(n+1)] #teamId , solved, total_time

for team in range(1,n+1):
    for Id in range(1, m+1):
        if rank[team][Id][0] != 301:
            grade[team][1] += 1
            grade[team][2] += (rank[team][Id][0] + rank[team][Id][1])

# 맞힌 문제 내림차순 정렬 (-grade[1]), 총 시간 오름차순 정렬 (grade[2]), 팀 번호 오름차순 정렬(grade[0])
# 적용하고 싶은 순서대로 정렬하는 파이썬 기법
# sorted(item , key = labda x: (x[0], -x[1])) 부호에 따라 오름차순인지 내림차순인지 결정
# 인덱스 순서도 변경 가능

grade = sorted(grade[1:],key = lambda x: (-x[1], x[2], x[0]))
# 각 팀의 등수는 문제를 많이 푼 순으로 산정된다. -> 문제 푼 횟수 내림차순
# 만약 푼 문제 수가 같을 경우 ‘총 시간’이 작은 순으로 산정된다. -> 총시간 오름차순
# 만약 순위가 같으면 팀 번호가 빠른 것을 먼저 출력한다. -> 팀 번호 오름차순
for i in grade:
    print(*i)