import sys
input = sys.stdin.readline

def factorial(number):
    value = 1

    for i in range(1, number + 1):
        value *= i

    return value

def combi(a, b):
    return int(factorial(a) / (factorial(b) * factorial(a - b)))

for tc in range(int(input())):
    N, M = map(int, input().split())

    dp = [[1] * (N+1) for _ in range(M+1)]
    
    for i in range(N, M):
        dp[i+1][N] = dp[i][N] + combi(i, N-1)

    print(dp[M][N])