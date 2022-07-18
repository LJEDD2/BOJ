n = int(input())
str_n = ''
while True:
    n+=1
    str_n = str(n)
    if str(n) == str_n[::-1]:
        print(n)
        break