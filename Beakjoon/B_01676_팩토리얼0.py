import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

def factorial(number):
    value = 1

    for i in range(1, number + 1):
        value *= i

    return value

target = str(factorial(N))

cnt = 0

for i in range(len(target)-1, -1, -1):
    if target[i] == '0':
        cnt += 1
    else:
        break

print(cnt)