while True:
    s = input()
    size = len(s)
    if s == '*':
        break

    flag = 0
    for d in range(1, size):
        word = []
        for i in range(size - d):
            word.append(s[i] + s[i + d])
        for i in word:
            print(word.count(i))
            if word.count(i) > 1:
                flag = 1
    if not flag:
        print(f"{s} is surprising.")
    else:
        print(f"{s} is NOT surprising.")
