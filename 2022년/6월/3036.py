def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

n = int(input())
n_list = list(map(int,input().split()))

for i in n_list[1:]:
    r = gcd(n_list[0], i)
    print('{}/{}'.format(n_list[0]//r, i//r))

