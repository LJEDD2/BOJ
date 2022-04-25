n = list(input())
m = list(input())
count = 0

while count < len(n):
    if n[count] in m:
        m.remove(n[count])
        n.remove(n[count])
        count -= 1
    count += 1

print(len(n)+len(m))
