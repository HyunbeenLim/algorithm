import sys
sys.stdin = open('./sample_input.txt', 'r')

N, M = map(int, input().split())

ma = []
sam = []

ans = ''

for _ in range(N):
    ma.append(input())

for _ in range(M):
    temp = input()
    if temp in ma:
        ans += temp + ' '
    sam.append(temp)

if ans == '':
    ans = 'NO!!'

print(ans)