l = input()
ans = []
for i in range(len(l)):
    ans.append(l[i:])
print(*sorted(ans), end='\n')