x,y,w,s = map(int,input().split())
result = []
maxv = max(x,y)
minv = min(x,y)

if 2*w > s:
    if w < s:
        result.append((minv * s) + (maxv - minv) * w)
    else:
        if (x+y)%2 == 0:
            result.append(maxv*s)
        else:
            result.append((maxv-1)*s + w)
else:
    result.append((x+y)*w)

print(*result)