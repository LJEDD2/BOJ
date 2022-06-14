n = int((input()[:-2]+'00'))
f = int(input())

while True:
    if n%f == 0:
        print(str(n)[-2:])
        break
    n += 1
