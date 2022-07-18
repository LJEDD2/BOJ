import re

words = []
while True:
    words.extend(input().split())
    if words[-1] == 'E-N-D':
        break
result = []
for i in words:
    result.append(re.sub('[^a-z-]','',i.lower()))

print(sorted(result,key=lambda x : len(x),reverse = True)[0])