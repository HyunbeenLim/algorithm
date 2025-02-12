import sys
sys.stdin = open('input.txt', 'r')

def factorial(number):
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value

for tc in range(int(input())):
    N, M = map(int, input().split())

    dp = [[0] * N for _ in range(M)]
    


    print(f'#{tc}')
    print()