emp = [list(map(int, input().split())) for i in range(3)]
ans = 0
for i in range(3):
    ans = (emp[i][3]*3600 - emp[i][0]*3600) + (emp[i][4]*60-emp[i][1]*60) + (emp[i][5]-emp[i][2])
    print(ans//3600 , ans%3600//60, ans%3600%60)