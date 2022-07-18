age = int(input("한국 나이를 입력해주세요 : "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
my_usa_age = age - 1 + birth
print(f"미국 나이는 {my_usa_age}살 입니다")