import math
def solve(n):
    result = set()
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0 :
            result.add(i)
            result.add(n//i)

    result = sorted(result)
    if sum(result[:-1]) == n:
        print(result[-1],'= ',end = "")
        print(*result[:-1],sep=' + ')
    else:
        print(result[-1],"is NOT perfect.")

while 1:
    n = int(input())
    if n == -1:
        break
    solve(n)