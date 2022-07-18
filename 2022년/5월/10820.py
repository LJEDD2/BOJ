while True:
    try:
        answer = [0,0,0,0]
        temp = input()
        for i in temp:
            if i.islower():
                answer[0] += 1
            elif i.isupper():
                answer[1] += 1
            elif i.isnumeric():
                answer[2] += 1
            elif i.isspace():
                answer[3] += 1
        print(*answer)
    except EOFError:
        break