def permutation():
    if len(result) == n:
        print(*result)
        return

    for i in range(1,n+1):
        if i not in result:
            result.append(i)
            permutation()
            result.pop()

n = int(input())
result = []
permutation()