n,d = map(int,input().split())
word = ''
for i in range(1,n+1):
    word += str(i)
print(word.count(str(d)))
    
