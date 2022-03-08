h , m = map(int, input().split())
total = h * 60 + int(input())
#60분으로 나눈 걸 24를 다시 나눠서 그 나머지로 시간을 표현한다. 0~24시
print(total//60%24, t%60)