while True:
    a,b = map(int,input().split())
    if [a,b] == [0,0]:
        break
    else:
        if a < b:
            if b % a == 0:  # 약수 인 경우
                print("factor")
            else:
                print("neither")
        elif a > b:
            if a % b == 0:  # 배수 인 경우
                print("multiple")
            else:
                print("neither")
        else:
            print("neither")
