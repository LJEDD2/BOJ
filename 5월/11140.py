alpha = 'abcdefghijklmnopqrstuvwxyz'
def islxl(word):
    for x in alpha:
        if 'l'+x+'l' in word:
            return True
    return False

for _ in range(int(input())):
    word = input()
    if "lol" in word:
        print(0)
    elif "lo" in word or "ol" in word or "ll" in word or islxl(word):
        print(1)
    elif "l" in word or "o" in word:
        print(2)
    else:
        print(3)
