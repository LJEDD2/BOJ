def Erasto(m):
    prime = [False, False] + [True] * (2*m - 1)
    for i in range(2,2*m+1):
        if prime[i]:
            for j in range(i*2, 2*m+1, i ):
                prime[j] = False
    # m보다 크고 2*m보다 작거나 같은 True 개수
    print(prime[m+1:2*m+1].count(True))

while True:
    n = int(input())
    if n == 0:
        break
    Erasto(n)
