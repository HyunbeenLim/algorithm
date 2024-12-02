import sys
input = sys.stdin.readline

n = int(input())
sequence = [0] * n

for _ in range(n):
    sequence.append(int(input()))

# 스택
stack = []
# 스택에 넣을 숫자
num = 1
result = True
ans = []

for i in range(n):
    # 해당 반복의 수열의 요소
    curr = sequence[i]
    # 그 요소가 다음에 등장할 숫자보다 크거나 같으면 그 숫자까지 스택에 쌓아줘야 함
    if curr >= num:
        while curr >= num:
            ans.append('+')
            num += 1
            stack.append(num)
        # 해당 숫자까지 쌓고 pop(수열 만들기)
        stack.pop()
        ans.append('-')
    
    # 그 외의 경우
    else:
        top = stack.pop()
        # 스택 가장 위 숫자가 수열의 요소보다 크면, 수열 만들기 불가능
        if top > curr:
            print('NO')
            result = False
            break
        else:
            ans.append('-')

if result:
    for to_print in ans:
        print(to_print)

# 런타임 에러