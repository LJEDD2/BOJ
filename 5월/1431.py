def sumv(s):
    result = 0
    for i in s:
        if i.isdigit():
            result+=int(i)
    return result

s_list = []
for i in range(int(input())):
    s_list.append(input())

print(*sorted(s_list,key = lambda x : (len(x), sumv(x), x)),sep='\n')
