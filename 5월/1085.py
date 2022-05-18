x,y,w,h = map(int,input().split())
nlist = [x,y,w-x,h-y]
print(min(nlist))
