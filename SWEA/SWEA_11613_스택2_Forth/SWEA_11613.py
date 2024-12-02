import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_11613_스택2_Forth/sample_input.txt', 'r')

lst = ['+', '-', '/', '*']

def calculate(qus):
    stack = []
    for token in qus:
        if token in lst:
            # 스택에 숫자가 두개보다 작은데 연산자를 만난 경우
            if len(stack) < 2:
                return 'error'
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+': stack.append(a+b)
                elif token == '-': stack.append(a-b)
                elif token == '/': stack.append(a//b)
                else: stack.append(a*b)
        elif token == '.':
            # 수식을 마치는 . 을 만났는데, 숫자가 두개 이상 남아있으면 형식이 잘못된 것
            if len(stack) != 1:
                return 'error'
            else:
                return stack.pop()
        else:
            stack.append(int(token))

t = int(input())

for tc in range(1, t + 1):
    qus = input().split()
    ans = calculate(qus)
    print(f'#{tc} {ans}')