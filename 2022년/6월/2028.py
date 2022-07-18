def solve(n):
    n_idx = len(str(n))
    n_square = str(n**2)
    if n_square[-n_idx:] == str(n):
        print("YES")
    else:
        print("NO")

for i in range(int(input())):
    solve(int(input()))