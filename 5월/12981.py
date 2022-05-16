R,G,B = map(int,input().split())
minv = min(R,G,B)
R -= minv
G -= minv
B -= minv
result = [R//3,G//3,B//3,minv]
R %= 3
G %= 3
B %= 3

if R == 2:
    R = 0
    result[0] += 1
if G == 2:
    G = 0
    result[1] += 1
if B == 2:
    B = 0
    result[2] += 1
if R or G or B > 0:
    result[3] += 1

print(sum(result))
