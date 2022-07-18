#-조합을 활용한 이항계수 공식-#
#           n!           #
# ---------------------- #
#      k! (n - k) !      #


def factorial(n):
    if n <= 1:
        dp[n] = 1
        return dp[n]
    else:
        dp[n] = n * factorial(n-1)
        return dp[n]

n, k = map(int,input().split())
dp = [0] * (n+1)
print(factorial(n)//(factorial(k)*factorial(n-k)))