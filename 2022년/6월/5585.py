# 500 100 50 10 5
money = 1000 - int(input())
count = 0
while money > 0 :
    for i in [500,100,50,10,5,1]:
        while money >= i:
            money -= i
            count += 1
print(count)