import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input()
    s = input().split()
    card = s[0]

    for i in s[1:]:
        if card[0] >= i :
            card = i + card
        else:
            card += i
    print(''.join(card))