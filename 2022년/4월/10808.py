word = [0]*26
s = input()
for i in s:
    word[ord(i)-97] += 1
print(*word)