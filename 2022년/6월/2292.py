n = int(input())
a = 1
d = 1

while True:
    a += 6 * d
    d += 1
    if n <= a:
        print(d)
        break
