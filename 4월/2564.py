m, n = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(int(input())+1)]
dg = location.pop()
#  둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고,
#  상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리
result = 0

if dg[0] == 1: # 동근이가 북쪽 라인에 있고
    for dir, distance in location:
        if dir == 1 : # 상점이 북쪽일 때
            result += abs(dg[1] - distance)
        elif dir == 2: # 상점이 남쪽일 때
            l_dis = dg[1] + n + distance
            r_dis = (m - dg[1]) + n + (m - distance)
            result += min(l_dis , r_dis)
        elif dir == 3: # 상점이 서쪽일 때
            result += dg[1] + distance
        elif dir == 4: # 상점이 동쪽일 떼
            result += (m - dg[1]) + distance

elif dg[0] == 2:
    for dir, distance in location:
        if dir == 1 :
            l_dis = dg[1] + n + distance
            r_dis = (m - dg[1]) + n + (m - distance)
            result += min(l_dis, r_dis)
        elif dir == 2:
            result += abs(dg[1] - distance)
        elif dir == 3:
            result += dg[1] + (n - distance)
        elif dir == 4:
            result += (m - dg[1]) + (n - distance)

elif dg[0] == 3:
    for dir, distance in location:
        if dir == 1 :
            result += dg[1] + distance
        elif dir == 2:
            result += (n - dg[1]) + distance
        elif dir == 3:
            result += abs(dg[1] - distance)
        elif dir == 4:
            l_dis = dg[1] + m + distance
            r_dis = (n - dg[1]) + m + (n - distance)
            result += min(l_dis, r_dis)

elif dg[0] == 4:
    for dir, distance in location:
        if dir == 1 :
            result += dg[1] + (m - distance)
        elif dir == 2:
            result += (n - dg[1]) + (m - distance)
        elif dir == 3:
            l_dis = (n - dg[1]) + m + (n - distance)
            r_dis = dg[1] + m + distance
            result += min(l_dis, r_dis)
        elif dir == 4:
            result += abs(dg[1] - distance)

print(result)
