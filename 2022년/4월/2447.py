def solution(n):
    if n == 3:
        return ['***','* *','***']

    else:
        star = solution(n//3)
        s = []

        for i in star:
            s.append(i*3)

        for i in star:
            s.append(i + " "*(n//3) + i)

        for i in star:
            s.append(i*3)

        return s

n = int(input())
star = solution(n)

for i in star:
    print(''.join(i))
