def solution(n):
    dp = [0] * (n + 1)
    if n >= 2:
        dp[0] = 1
        dp[2] = 3
        for idx in range(4, n+1, 2):
            dp[idx] = (dp[idx-2] * 4 - dp[idx-4]) % 1000000007

    return dp[n]

'''
점화식
f(n) = 4 * f(n-2) - f(n-4)    이걸 대체 어떻게 찾냐...
'''