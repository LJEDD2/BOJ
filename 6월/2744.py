word = ''
s = input()
for i in s:
    if i.isupper():
        word += i.lower()
    else:
        word += i.upper()
print(word)

#print(s.swapcase())
