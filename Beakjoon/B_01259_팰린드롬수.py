import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

while True:
    number = input().strip()
    if number == '0':
        break
    start = 0
    end = len(number) - 1

    while start <= end:
        if number[start] != number[end]:
            break
        start += 1
        end -= 1

    if start > end:
        print('yes')
    else:
        print('no')
