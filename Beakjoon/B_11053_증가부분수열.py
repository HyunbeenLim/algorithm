import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def count_longest():
    dp = [1] * A

    for i in range(A):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

A = int(input())
numbers = list(map(int, input().split()))

ans = count_longest()

print(ans)