import sys
input = sys.stdin.readline

N, M = map(int, input().split())

number_list = list(map(int, input().split()))
S_list = [0] * N
S_list[0] = number_list[0]
for i in range(1, N):
    S_list[i] = S_list[(i-1)] + number_list[i] # 구간 합 리스트

for _ in range(M):
    a, b = map(int, input().split())
    if (a - 1) == 0:
        print(S_list[(b - 1)])
    else:
        print(S_list[(b - 1)] - S_list[(a - 2)])