import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_list = list(map(int, input().split()))

S_list = [0] * N
S_list[0] = number_list[0]
C_list = [0] * M

ans = 0
for i in range(1, N):
    S_list[i] = S_list[(i-1)] + number_list[i] # 구간 합 리스트

for i in range(N):
    remainder = S_list[i] % M
    if remainder == 0:
        ans += 1
    C_list[remainder] += 1

for j in range(M):
    if C_list[j] > 1:
        ans += ((C_list[j] * (C_list[j] - 1)) // 2)

print(ans)