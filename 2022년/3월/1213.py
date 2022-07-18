name = input()
name_dic = {}
for i in range(len(name)):
    if name[i] in name_dic:
        name_dic[name[i]] += 1
    else:
        name_dic[name[i]] = 1

#[('A', 6), ('V', 6), ('C', 1)] 형태로
letters = []
for letter in name_dic:
    letters.append((letter,name_dic[letter]))
#정렬 먼저
letters.sort()

break_cnt = 0
Palindrome = ""
center = ""
for letter in letters:
    # 개수가 홀수인 알파벳이 여러개면 break
    if letter[1]%2 != 0:
        break_cnt += 1
        #홀수인 알파벳이 센터에 오게 될 것
        center += letter[0]
    # 같은게 2개 이상이면
    # 반쪽만 일단 만들어주자 + 사전 순
    Palindrome += letter[0]*(letter[1]//2)

if break_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(Palindrome + center + Palindrome[::-1])

