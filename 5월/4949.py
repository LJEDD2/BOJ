def solve(s):
    stack = []
    flag = False
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack.pop() != '(':
                    flag = True
                    break
            else:
                flag = True
                break

        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack:
                if stack.pop() != '[':
                    flag = True
                    break
            else:
                flag = True
                break

    if stack or flag:
        print("no")
    else:
        print("yes")


while True:
    s = input()
    if s == '.':
        break
    solve(s)