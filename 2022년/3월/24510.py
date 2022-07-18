s_list = [input() for _ in range(int(input()))]

maxv = []
for i in s_list:
    maxv.append(i.count('for') + i.count('while'))
print(max(maxv))
