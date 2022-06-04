b_cnt = 0
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global b_cnt
    f[1] = f[2] = 1;
    for i in range(3,n+1):
        b_cnt += 1
        f[i] = f[i - 1] + f[i - 2]; 
    return b_cnt

n = int(input())
f = [0]*(n+1)
print(fib(n),fibonacci(n))
