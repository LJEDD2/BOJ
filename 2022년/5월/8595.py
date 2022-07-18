import re
for _ in range(2): n = input()
print(sum(list(map(int,re.findall("\d+",n)))))