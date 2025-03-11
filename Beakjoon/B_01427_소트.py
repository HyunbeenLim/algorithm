import sys
input = sys.stdin.readline

numbers = list(input().strip())
numbers.sort()
numbers.reverse()

for number in numbers:
    print(number, end='')