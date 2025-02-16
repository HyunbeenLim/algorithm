import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def count_longest():
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if numbers[j] > numbers[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

N = int(input())
numbers = list(map(int, input().split()))

ans = count_longest()

print(ans)