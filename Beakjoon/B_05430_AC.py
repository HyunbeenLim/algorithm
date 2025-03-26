import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque

for _ in range(int(input())):
    order = input().strip()
    N = int(input())
    input_string = input().strip()
    input_string = input_string.strip('[]')
    input_string = input_string.split(',')

    numbers = deque()

    for f in input_string:
        # 빈 리스트를 input 받았을 때가 있을 수도 있음
        try:
            num = int(f)
            numbers.append(num)
        except ValueError:
            continue
    
    check = True
    reverse_flag = False

    for s in order:
        if s == 'R':
            reverse_flag = not reverse_flag
        elif s == 'D':
            if numbers:
                if reverse_flag:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                check = False
                break

    if check:
        numbers = reversed(numbers) if reverse_flag else numbers
        print('[' + ','.join(map(str, numbers)) + ']')
    else:
        print('error')