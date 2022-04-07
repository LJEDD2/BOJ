n = int(input())
sss = '666'
num = cnt = 0
while True:
    num += 1
    if sss in str(num):
       cnt +=1
    if cnt == n:
        print(num)
        break

