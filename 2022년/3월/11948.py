A = sorted([int(input()) for _ in range(4)],reverse=True)
B = sorted([int(input()) for _ in range(2)],reverse=True)
print(sum(A[:3])+B[0])