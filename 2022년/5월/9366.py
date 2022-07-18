for i in range(1,int(input())+1):
    a, b, c = map(int, input().split())
    maxv = max(a,b,c)
    print("Case #{}: ".format(i),end="")
    if a + b + c - maxv <= maxv:
        print("invalid!")
    elif a == b == c:
        print("equilateral")
    elif a == b or b == c or a == c:
        print("isosceles")
    else:
        print("scalene")
