for i in range(int(input())):
    n_list = list(map(int,input().split()))
    sumv , minv = 0, 101
    for i in n_list:
        if not i%2:
            minv = min(minv,i)
            sumv += i
    print(sumv,minv)