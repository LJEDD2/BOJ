while True:
    s = input()
    if s == '#':
        break
    for i in s.split():
        print(i[::-1],end=" ")
    print()