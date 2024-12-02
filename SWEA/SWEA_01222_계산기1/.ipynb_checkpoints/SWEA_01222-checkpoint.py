import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01222_계산기1/input.txt', 'r')

icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack에 push하기 전
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택에 내부

for j in range(1, 11):
    N = int(input())
    infix = input()

    postfix = ''
    stack = []
    # 후위식 변경
    for token in infix:
        if token in icp:
            if token == '+':
                # icp가 isp보다 커질 때 까지 pop, stack에 뭐가 있어야 비교 함
                while stack and icp[token] <= isp[stack[-1]]:
                    postfix += stack.pop()
                # 그 외엔 push
                stack.append(token)
        else:
            # 피연산자
            postfix += token
    while stack:
        postfix += stack.pop()

    # 계산
    for token in postfix:
        if token in icp:
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
        else:
            # 피연산자
            stack.append(int(token))

    print(f'#{j} {stack.pop()}')




