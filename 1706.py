n , m = map(int,input().split())
board = [list(input()) for _ in range(n)]

word_list_row = []
for i in range(n):
    word = ""
    for j in range(m):
        if board[i][j] != '#':
            word += board[i][j]
        else:
            if len(word) > 1:
                word_list_row.append(word)
                word = ""
            else:
                word =""
    if len(word) > 1:
        word_list_row.append(word)

word_list_col = []
for i in range(m):
    word = ""
    for j in range(n):
        if board[j][i] != '#':
            word += board[j][i]
        else:
            if len(word) > 1:
                word_list_col.append(word)
                word = ""
            else:
                word =""
    if len(word) > 1:
        word_list_col.append(word)


print(sorted(word_list_row + word_list_col)[0])
