def Eratos(n,m):
    # n 까지 모두 소수라고 처음에 가정
    prime = [False,False] + [True] * (n-1)
    cnt = 0
    for i in range(2,n+1):
            for j in range(i, n+1, i): # 10까지 i포함 i의 배수를 찾아서 제거 i+=i
                if prime[j]:  # 소수일 경우
                    prime[j] = False
                    cnt += 1
                    if cnt == m:
                        print(j)
                        break


n, m =map(int,input().split())
Eratos(n,m)
