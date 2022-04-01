h , w = map(int,input().split())
bar = list(map(int,input().split()))
sumv = 0

for i in range(1, max(bar)+1): # 높이만큼 탐색하면서 빈칸세줌
    flag = False
    temp = 0
    for j in range(w):
        if bar[j] >= i:
            sumv += temp
            flag = True # 현재 높이와 같거나 보다 더 큰 기둥이 존재한다.
            temp = 0
        elif flag: # bar[j]보다 큰 기둥이 있었고 이거보다 더 작은 공간이 있을 때
            temp += 1

print(sumv)


