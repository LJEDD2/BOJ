n = int(input())
for i in range(n):
    s = input()
    # Two pointer
    left = 0
    right = len(s) - 1
    result = 0
    while left < right : # 중간지점까지 돌거임
        # 두 문자가 같으면 그냥 지나가기
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1 :
                word = s[:right] + s[right+1:] # 오른쪽 문자 제거
                print('r >>',word)
                if word == word[::-1]:
                    result = 1
                    break

            if left + 1 < right:
                word = s[:left] + s[left+1:]  # 왼쪽 문자 제거
                print('l >>',word)
                if word == word[::-1]:
                    result = 1
                    break
            result = 2
            break

    print(result)




