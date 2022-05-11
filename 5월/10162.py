T = int(input())
A,B,C = 300,60,10

if T % C:
    print(-1)
else:
    button = [0,0,0]
    if T >= A:
        button[0] = T//A
        T %= A
    if T >= B:
        button[1] = T//B
        T %= B
        button[2] = T//C

print(*button)
