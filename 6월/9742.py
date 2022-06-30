def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(string, idx):
    global cnt
    if idx == len(a):
        cnt += 1
        if cnt == b:
            return string

    for k in a:
        if k not in string:
            result = permutation(string + k, idx + 1)
            if result:
                return result


while True:
    try:
        a, b = input().split()
        b = int(b)
        size = len(a)
        cnt = 0

        if factorial(size) < b:
            print(f'{a} {b} = No permutation')
        else:
            print(f'{a} {b} = {permutation("",0)}')
    except EOFError:
        break
