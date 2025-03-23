import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))

ans = [-1] * N  # 결과를 미리 -1로 채워 놓음
stack = []

for i in range(N - 1, -1, -1):  # 뒤에서부터 시작
    
    # 현재 원소보다 작거나 같은 애들은 오큰수가 될 수 없으므로 제거
    while stack and stack[-1] <= numbers[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] 
    stack.append(numbers[i])  

print(*ans)