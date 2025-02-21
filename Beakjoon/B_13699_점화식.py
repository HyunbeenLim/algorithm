import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[N])

'''
t(0) = 1
t(1) = 1


t(n) = t(0) * t(n-1) + t(1) * t(n-2) + ... + t(n-2) * t(1) + t(n-1) * t(0)
'''