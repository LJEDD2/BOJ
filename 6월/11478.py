a = input()
result = []
for i in range(len(a)):
    for j in range(i,len(a)):
        result.append(a[i:j+1])
print(len(set(result)))
