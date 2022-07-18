def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(string):
    global cnt
    if len(string) == size:
        cnt += 1
        #print('>>>>>>',cnt,string)
        if cnt == b:
            print(f'{a} {b} = {string}')
            return

    for k in range(size):
        if not visited[k]:
            visited[k] += 1
            permutation(string + a[k])
            visited[k] -= 1


while True:
    try:
        a, b = input().split()
        b = int(b)
        size = len(a)
        cnt = 0
        visited = [0] * size

        if factorial(size) < b:
            print(f'{a} {b} = No permutation')
        else:
            permutation('')

    except EOFError:
        break

