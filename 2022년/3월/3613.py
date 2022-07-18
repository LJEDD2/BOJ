text = input()
Cpp = JAVA = []
word = []

#C++ -> JAVA
if '_' in text:
    # error case #1 : 첫번째와 마지막 문자가 _ 일때
    # error case #2 : __가 2개 이상 연속으로 입력될 때
    # error case #3 : C++에서 Java로 변환할 때 대문자가 입력된 경우
    if text[0] == "_" or text[-1] == "_" or "__" in text:
        print("Error!")
    else:
        # flag를 통해 대문자가 포함되었는지 판별해서 error인지 아닌지 구분
        flag = False
        for i in text:
            if i.isupper():
                flag = True
                break
        if flag == True:
            print("Error!")
        else:
            Cpp = text.split('_')
            # .capitalize() 를 통해 '_' 다음 단어의 맨 앞 문자 대문자로 변환
            print(Cpp[0]+''.join([i.capitalize() for i in Cpp[1:]]))

#JAVA -> C++
else:
    # error case #4 : 맨 앞자리 문자가 소문자일 경우
    # 출력조건
    # JAVA -> C++의 경우 단어를 구분할 때 대문자를 마주치면 split()
    # 저장한 word를 하나의 단어로 묶어 _를 추가해준 뒤 출력
    # 모두 소문자로 변환

    if text[0].isupper():
        print("Error!")
    else:
        word = ''
        JAVA = []
        for i in text:
            if i.isupper():
                JAVA.append((word+'_').lower())
                word = ''
            word += i
        #마지막 단어
        JAVA.append(word.lower())
        print(''.join(JAVA))
