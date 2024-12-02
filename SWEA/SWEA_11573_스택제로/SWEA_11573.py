import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_11573_스택제로/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))

    stack = [0] * N
    top = -1

    for i in range(N):
        # 1 이면 push, 0 이면 pop
        if number_list[i]:
            top += 1
            stack[top] = number_list[i]
        # sum 을 구해주어야 해서 top = 0 먼저 하기
        else:
            stack[top] = 0
            top -= 1
    
    print(f'#{tc} {sum(stack)}')

    