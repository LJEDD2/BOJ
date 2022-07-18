n = int(input())
n_list = list(map(int,input().split()))
s_list = sorted(set(n_list))
n_dic = {s_list[i] : i for i in range(len(s_list))}
print(*[n_dic[i] for i in n_list])