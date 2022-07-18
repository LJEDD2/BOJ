n_str = input()
num=[]
for i in n_str.split('-'):
    num.append(list(map(int, i.split("+"))))

ans = sum(num[0])
for i in num[1:]:
    ans -= sum(i)

print(ans)
