for _ in range(int(input())):
    score=[0]*2
    for _ in range(9):
        y,k=map(int,input().strip().split())
        score[0]+=y
        score[1]+=k
    print("Yonsei" if score[0]>score[1] else "Korea" if score[0]<score[1] else "Draw")
