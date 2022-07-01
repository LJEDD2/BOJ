def permutation(N):
    if N == n:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            result[N] = i+1
            permutation(N+1)
            visited[i] = 0


n = int(input())
visited = [0] * n
result = [0] * n
permutation(0)
