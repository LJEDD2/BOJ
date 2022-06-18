import string

alpha = ' ' + string.ascii_lowercase + string.ascii_uppercase
sumv = 0
for i in input():
    sumv += alpha.index(i)

prime = [False,True]+[True]*(sumv-1)
for i in range(2,sumv+1):
    if prime[i]:
        for j in range(2*i,sumv+1,i):
            prime[j] = False

if prime[sumv]:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
