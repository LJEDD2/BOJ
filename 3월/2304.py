p_list = sorted([list(map(int, input().split())) for _ in range(int(input()))])
max_p = max(p_list, key=lambda x: (x[1]))

ans_l = 0
prev = 0

if len(p_list) == 1 :
    print(max_p[1])
    exit(0)

for i in range(len(p_list)):
    if p_list[i][1] == max_p[1]:
        ans_l += (p_list[i][0] - p_list[prev][0]) * p_list[prev][1]
        temp = i
        break
    elif p_list[i][1] > p_list[prev][1]:
        ans_l += (p_list[i][0] - p_list[prev][0]) * p_list[prev][1]
        prev = i

ans_r = 0
prev = len(p_list) - 1
middle = 0

for i in range(len(p_list) - 1, 0, -1):
    if p_list[i][1] == max_p[1]:
        ans_r += abs(p_list[i][0] - p_list[prev][0]) * p_list[prev][1]
        middle += (p_list[i][0] - p_list[temp][0] + 1) * max_p[1]
        break
    elif p_list[i][1] > p_list[prev][1]:
        ans_r += abs(p_list[i][0] - p_list[prev][0]) * p_list[prev][1]
        prev = i

print(ans_l + ans_r + middle)
