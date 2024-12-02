import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12390_부분집합_재귀/sample_input.txt', 'r')

def subset(k, n):
    global cnt
    if k == n:
        sub_sum = 0
        sub_ele = 0

        for i in range(n):
            if bit[i]:
                sub_ele += 1
                sub_sum += A_set[i]
        if sub_ele == N and sub_sum == K:
            cnt += 1
    else:
        bit[k] = 0
        subset(k + 1, n)
        bit[k] = 1
        subset(k + 1, n)

    return cnt

T = int(input())

for tc in range(1, T + 1):
    M = 12
    bit = [0] * M
    A_set = list(range(1, M + 1))

    N, K = map(int, input().split())
    cnt = 0
    subset(0, M)

    print(f'#{tc} {cnt}')






