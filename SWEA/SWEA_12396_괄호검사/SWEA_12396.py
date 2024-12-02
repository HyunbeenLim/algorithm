import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12396_괄호검사/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    string = input()
    
    stack = [0] * len(string)
    top = -1

    ans = 1
    # {: 1, (:2 가 쌓이게 함
    ## 닫는 괄호가 나왔을 때, 괄호의 해당 숫자가 top에 위치하지 않는다면 반복 중지 후 0
    for char in string:
        if char == '{':
            top += 1
            stack[top] = 1
        elif char == '(':
            top += 1
            stack[top] = 2
        elif char == '}':
            if stack[top] != 1:
                ans = 0
                break
            else:
                top -= 1
        elif char == ')':
            if stack[top] != 2:
                ans = 0
                break
            else:
                top -= 1

    # 괄호가 다 닫히지 않은 경우
    if top != -1:
        ans = 0
    
    print(f'#{tc} {ans}')


T = int(input())

for tc in range(1, T+1):

    arr = input()
    S = []
    top = -1
    is_ok = 1
    bracket = {'(' : ')', '[':']', '{':'}'}

    for i in arr:
        if i in bracket.keys():
            S.append(i)       # 여는괄호 경우 : top의 인덱스 값에 여는 괄호를 stack에 기록(push)
            # print(S)
        elif i in bracket.values():         # 닫는 괄호 경우 :
            if i == bracket.get(S[-1]): # 비어있지않고 짝이 같으면,
                S.pop() # 마지막 값 사라짐
                 # 제일 높은 인덱스를 낮춰주기
                # print(S)
            else:
                is_ok = 0

    if len(S) != 0:
        is_ok = 0 #반복이 끝나도 스택이 비어있지않으면 에러임.

    print(f'#{tc} {is_ok}')


