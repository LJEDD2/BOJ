# 화폐단위 변경 *100
def solve(n):
    money = {25:0,10:0,5:0,1:0}
    while n > 0:
        for i in money.keys():
            while n >= i:
                n -= i
                money[i] += 1
    print(*money.values())

for i in range(int(input())):
    solve(int(input()))