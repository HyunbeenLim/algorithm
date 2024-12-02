## 스택 안 쓴거 - 내 코드

import copy

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input())

    for i in range(1, N + 1):
        new_list = [1] * i
        if len(new_list) == 1 or len(new_list) == 2:
            print(*new_list)
        else:
            for j in range((len(old_list) - 1)):
                new_list[j + 1] = old_list[j] + old_list[j + 1]
            print(*new_list)

        old_list = copy.deepcopy(new_list)


## 현준이형 스택 쓴 거

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stack = []
    
    print(f'#{tc}')
    for _ in range(N):
        # 0 == 미할당 상태
        prev = 0  # 직전 항
        curr = 0  # 현재 항
        prev_stack = stack  # 출력을 위해 임시로 저장하는 stack
        stack = []  # 복사 후 stack 초기화
        
        # 탈출 조건: prev_stack이 비었을 때
        while prev_stack:
            prev = curr
            curr = prev_stack.pop()
            
            stack.append(prev + curr)
        
        # 맨 마지막 1 추가
        stack.append(1)
        
        # 매 회차마다 출력
        print(*stack)