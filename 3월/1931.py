p = sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x:(x[1],x[0]))
# 최대 사용할 수 있는 회의 개수
# 회의 시작시간과 끝 시간이 겹칠 수도 있다 -> 3,4 4,5 -> 끝나는 시간 기준으로 정렬해야한다.
# 앞 회의 끝나는 시간이랑 다음회의 시작시간이 안겹치게되려면 i-1 < i

end, cnt = 0, 0
for i in p:
    if i[0] >= end:
        end = i[1]
        cnt+=1

print(cnt)
