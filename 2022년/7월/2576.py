numbers = sorted([int(input()) for _ in range(7)])
ans = []
for i in numbers:
    if i%2:
        ans.append(i)

if ans:
    print(sum(ans),ans[0],sep='\n')
else:
    print(-1)