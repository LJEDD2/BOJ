n_list = sorted(set([input() for _ in range(int(input()))]),key = lambda x : (len(x),x))
print('\n'.join(n_list))
