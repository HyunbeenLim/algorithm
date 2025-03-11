import sys
input = sys.stdin.readline

N = int(input())
seq = [int(input()) for _ in range(N)]

ans = []
stack = []
current_number = 1
validity = True

for num in seq:
    while current_number <= num:
        stack.append(current_number)
        ans.append('+')
        current_number += 1
    if stack and stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        validity = False
        break

if validity:
    for s in ans:
        print(s)
else:
    print('NO')