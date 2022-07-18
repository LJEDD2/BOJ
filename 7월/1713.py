picture = {}

t = int(input())
r = int(input())
lst = list(map(int,input().split()))

for i in range(r):
    if picture.get(lst[i]):
        picture[lst[i]][0] += 1
    else:
        if len(picture) < t:
            picture[lst[i]] = [1,i]
        else:
            delete = sorted(picture.items(), key = lambda x : (x[1][0], x[1][1]))[0][0] # 정렬 우선순위 : 추천횟수, 들어온 순서
            #print(delete,picture,picture[delete])
            del(picture[delete])
            picture[lst[i]] = [1,i]

print(*sorted(picture.keys()))
