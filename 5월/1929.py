def Erasto(n,m):
    flag = [False,False] + [True] * (m-1)

    for i in range(2,m+1):
        if flag[i] :
            if i >= n:
                print(i)
            for j in range(i*2 , m+1, i):
                flag[j] = False

Erasto(*map(int,input().split()))
