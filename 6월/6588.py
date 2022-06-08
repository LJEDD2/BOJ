n = 1000000
prime = [False,False] + [True]*(n-1)
for i in range(2, n + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = False

def goldbach(num):
    for i in range(2,num):
        if prime[i] and prime[num-i]:
            print('{} = {} + {}'.format(num,i,num-i))
            break


while True:
    num = int(input())
    if num == 0:
        break
    goldbach(num)
