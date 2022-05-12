def solve(s):
    flag = True
    ans = 0
    for i in s:
        if i == "(":
            ans += 1
        elif i == ")":
            ans -= 1
            if ans < 0:
                flag = False
                break

    if flag and ans == 0:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    s = input()
    solve(s)
