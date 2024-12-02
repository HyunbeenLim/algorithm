import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01225_암호생성기/input.txt', 'r')

from collections import deque

for i in range(1, 11):
    tc = int(input())
    numbers = deque(list(map(int, input().split())))

    # 뺄 숫자
    number_to_subtract = 0

    while True:
        number_to_subtract += 1
        # 뺄 수가 6에 다다르면 1로 초기화
        if number_to_subtract == 6:
            number_to_subtract = 1
        # pop 이후 숫자 먼저 빼주기
        first_number = numbers.popleft() - number_to_subtract

        # 뺀 숫자가 0보다 작다면 0으로 고정 후 while 문 탈출
        if first_number > 0:
            numbers.append(first_number)
        elif first_number <= 0:
            first_number = 0
            numbers.append(first_number)
            break

    print(f'#{tc}', *numbers)