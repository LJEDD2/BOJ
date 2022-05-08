# python에서 re API를 이용하면 문자열에서 숫자를 쉽게 추출할 수 있다.
# 다음과 같이 finall을 이용한다.
    #"\d+" : 숫자 묶음 단위 별로 추출
    #"\d" : 한자리 숫자 단위 별로 추출
import re

result = []
for _ in range(int(input())):
    word = input()
    number = re.findall("\d+",word)
    result += number
    result = list(map(int,result))

print(*sorted(result),sep='\n')
