nlist = []
for i in range(5):
    x = int(input())
    if x >= 40:
        nlist.append(x)
    else:
        nlist.append(40)

print(sum(nlist)//5)