number = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

def func(n):
    if n < 10:
        return number[n]
    return ' '.join([number[n//10],number[n%10]])

n, m = map(int,input().split())
num = []
for i in range(n,m+1):
    num.append([func(i),i])

num = sorted(num, key = lambda x : (x[0]))

while num:
    print(*map(lambda x : x[1], num[:10]))
    num = num[10:]

