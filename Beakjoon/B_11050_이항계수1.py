import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

N, K = map(int, input().split())

print(factorial(N) // (factorial(K) * factorial(N-K)))