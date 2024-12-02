import sys
sys.stdin = open('./sample_input.txt', 'r')

from collections import deque

N = int(input())

A = list(map(int, input().split()))

M = int(input())

lst = deque()

for _ in range(M):
    temp = input().split()
    if int(temp[2]) > 1:
        number = int(temp[2])
        for _ in range(number):
            lst.append(temp[0:2])
    else:
        lst.append(temp[0:2])

ans = ''

for i in range(N):
    cnt = 0
    for _ in range(A[i]):
        i_prob = lst.popleft()
        if i_prob[0] == 'ko' and int(i_prob[1]) >= 3:
            cnt += 1
    
    ans += str(cnt) + ' '

print(ans)