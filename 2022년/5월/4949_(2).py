while True :
    s = input()
    if s == '.' :
        break
    result = 0
    flag = True
    for i in s :
        if i == '(' :
            result += 1
        elif i == ')' :
            result -= 1
        elif i == '[' :
            result += 10000
        elif i == ']' :
            result -= 10000
        if result < 0 :
            flag = False
            break
    if result != 0 :
        flag = 0
    print("yes" if flag else "no")