for t in range(int(input())):
    n = int(input())
    result = n
    while n != 1:
        if n%2:
            n = n*3+1
            result = max(n,result)
        else:
            n = n//2

    print(result)
