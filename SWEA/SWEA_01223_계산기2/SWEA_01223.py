import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01223_계산기2/input.txt', 'r')

icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack에 push하기 전
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 내부

for tc in range(1, 11):
    N = int(input())
    infix = input()
    
    # 후위식 만들기
    postfix = ''
    stack = [] * (2 * N)
    top = -1

    for token in infix:
        if token in icp:
            # icp가 isp보다 커질 때 까지 pop, stack에 뭐가 있어야 비교 함
            while top >= 0 and icp[token] <= isp[stack[top]]:
                postfix += stack[top]
                top -= 1
            # 그 외 push
            top += 1
            stack[top] = token
        # 피연산자
        else:
            postfix += token

    # 계산하기
    stack = [] * (2 * N)
    top = -1

    for token in postfix:
        # 연산자 계산
        if token in icp:
            b = stack[top]
            top -= 1
            a = stack[top]
            top -= 1
            if token == '+':
                top += 1
                stack[top] = (a + b)
            elif token == '*':
                top += 1
                stack[top] = (a * b)
        # 피연산자
        else:
            top += 1
            stack[top] = int(token)

    print(f'#{tc} {stack[top]}')