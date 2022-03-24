n_list = sorted([int(input()) for i in range(int(input()))],reverse=True)

flag = False
for i in range(len(n_list)-2):
    if n_list[i] < n_list[i+1] + n_list[i+2]:
        print(sum(n_list[i:i+3]))
        flag = True
        break
if flag == False:
    print(-1)