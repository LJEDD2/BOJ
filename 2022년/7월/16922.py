from itertools import combinations_with_replacement as combi

rom = { 'I':1, 'V':5, 'X':10, 'L':50 }
n = int(input())
result = list(combi(rom.values(),n))
ans = []

for i in result:
    ans.append(sum(i))
print(len(set(ans)))
# n개 뽑는 조합 ? 모든 경우의 수


