numbers = sorted([ int(input()) for _ in range(int(input()))])
result = []

for i in range(len(numbers)):
    cnt = 0
    for j in range(numbers[i], numbers[i]+5):
        if j not in numbers:
            cnt += 1
    result.append(cnt)

print(min(result))

