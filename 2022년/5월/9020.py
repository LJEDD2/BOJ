def goldbach():
    n = int(input())
    prime = [False,False]+[True]*(n-1)
    result = []
    ans = []
    #에라토스테네스의 체
    for i in range(2,n+1):
        if prime[i]:
            result.append(i)
            for j in range(2*i, n+1, i):
                prime[j] = False

    """for i in range(2,n//2+1):
        if i in result and n-i in result:
            ans.append([i,n-i,(n-i)-i])"""

    ans = sorted(ans,key=lambda x : x[2])
    print(ans[0][0],ans[0][1])

for i in range(int(input())):
    goldbach()