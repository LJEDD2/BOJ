In = {}
Out = []
n = int(input())
for i in range(1,n+1):
    In[input()] = i
for i in range(1,n+1):
    Out.append(input())

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if In[Out[i]] > In[Out[j]]:
            count += 1
            break
print(count)
