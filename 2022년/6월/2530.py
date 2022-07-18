h,m,s = map(int,input().split())
r = int(input())
time = h*3600 + m*60 + s + r
print(time//3600%24,time//60%60,time%60)