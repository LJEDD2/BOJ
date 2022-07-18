def Intensity(r,g,b):
    i = r*2126 + g*7152 + b*722

    if 0 <= i < 510000:
        return '#'
    elif 510000 <= i < 1020000:
        return 'o'
    elif 1020000 <= i < 1530000:
        return '+'
    elif 1530000 <= i < 2040000:
        return '-'
    elif i >= 2040000:
        return '.'

n,m = map(int,input().split())

for i in range(n):
    row = list(map(int,input().split(' ')))

    for i in range(0,(m*3)-2,3):
        print(Intensity(row[i],row[i+1],row[i+2]),end='')
    print()
