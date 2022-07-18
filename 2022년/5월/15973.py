x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

if x1 > x3:
    x1,x3 = x3,x1
    y1,y3 = y3,y1
    x2,x4 = x4,x2
    y2,y4 = y4,y2

if x2 == x3:
    if y2 == y3 or y1 == y4:
        print("POINT")
    else:
        print("LINE")
elif x2 > x3: # y 높이에 따라서 NULL인지 LINE인지 FACE인지 결정
    if y2 < y3 or y1 > y4:
        print("NULL")
    elif y2 == y3 or y1 == y4:
        print("LINE")
    else:
        print("FACE")
elif x2 < x3:
    print("NULL")
