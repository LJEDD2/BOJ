# 노래가사 단어 수는 14개
n = int(input())
baby_shark = [0,"baby","sukhwan", "tururu", "turu",
              "very", "cute", "tururu", "turu",
              "in", "bed", "tururu", "turu",
              "baby", "sukhwan"]
q = n//14
r = n%14
cnt = 0
if r == 0:
    r = 14

# n%14 번째에 있는 문자열에서 ru 붙이면 됨.
if "ru" in baby_shark[r]:
    baby_shark[r] = baby_shark[r] + ("ru" * q)
    cnt = baby_shark[r].count("ru")
    if cnt >=5 :
        print("tu+ru*"+str(cnt))
    else:
        print(baby_shark[r])
else:
    print(baby_shark[r])
