n = dict()
for i in range(int(input())):
    s = ''.join(sorted(input()))
    if n.get(s):
        n[s] += 1
    else:
        n[s] = 1

print(len(n))