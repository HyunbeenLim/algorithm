import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01234_비밀번호/input.txt', 'r')

for tc in range(1, 11):
    N, *numbers = input().split()
    N = int(N)

    stack = [0] * N
    top = -1

    for num in numbers[0]:
        # top = -1 일 때  push
        if top == -1:
            top += 1
            stack[top] = num
        # 다음 수와 top 의 원소 비교 후 pop/push
        elif num == stack[top]:
            top -= 1
        elif num != stack[top]:
            top += 1
            stack[top] = num
    
    # 남은 비밀번호
    rest = stack[:(top + 1)]
    to_print = ''
    for char in rest:
        to_print += char

    print(f'#{tc} {to_print}')