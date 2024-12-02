T = int(input())

for tc in range(1, T + 1):
    string = input()
    N = len(string)
    
    stack = []
    cnt = 0
    idx = -1
    while idx < (N - 1):
        idx += 1
        if string[idx] == '(':
            # 레이저를 만나면 idx를 한번 점프한다
            # 남아 있는 열린 괄호만큼 cnt를 더해준다
            if string[idx + 1] == ')':
                idx += 1
                cnt += len(stack)
            else:
                stack.append(string[idx])
        # 막대가 끝나면 1 더해준다
        else:
            stack.pop()
            cnt += 1
    
    print(f'#{tc} {cnt}')
    
