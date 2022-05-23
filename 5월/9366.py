for i in range(1,int(input())+1):
    a, b, c = sorted(map(int, input().split()))
    if a + b <= c:
        print("Case #{}: invalid!".format(i))
    elif a == b == c:
        print("Case #{}: equilateral".format(i))
    elif a != b != c:
        print("Case #{}: scalene".format(i))
    else:
        print("Case #{}: isosceles".format(i))
