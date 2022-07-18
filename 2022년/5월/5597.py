n = [0]+sorted([int(input()) for _ in range(28)])
for i in range(1,31):
    if i not in n:
        print(i)
