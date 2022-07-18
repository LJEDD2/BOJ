def rectangle():
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    ans = 'a'
    # c
    if [x1, y1] == [x4, y4] or [x2, y1] == [x3, y4] or [x1, y2] == [x4, y3] or [x2, y2] == [x3, y3]:
        ans = 'c'
        return ans
    # d
    if x1 > x4 or y1 > y4 or x2 < x3 or y2 < y3:
        ans = 'd'
        return ans
    # b
    if x1 == x4 or x2 == x3 or y2 == y3 or  y1 == y4:
        ans = 'b'
        return ans

    return ans

for _ in range(4):
    print(rectangle())