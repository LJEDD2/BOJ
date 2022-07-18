import string
alpha = string.ascii_uppercase
a_dict = {}
for i in alpha:
    a_dict[i] = 0

s = input().upper()
for i in s:
    if i.isalpha():
        if a_dict.get(i):
            a_dict[i] += 1
        else:
            a_dict[i] = 1

for i in a_dict.keys():
    print(f"{i} | "+"*"*a_dict[i])