n = int(input())
alpha = {}
for i in range(n):
    s = input()
    if alpha.get(s[0]):
        alpha[s[0]] += 1
    else:
        alpha[s[0]] = 1
        
flag = 0
for i in sorted(alpha.items()):
    if i[1] >= 5:
        print(i[0],end="")
        flag = 1
        
if not flag:
    print("PREDAJA")
