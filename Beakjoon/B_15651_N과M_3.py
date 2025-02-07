# N개 중 M개를 고른 수열
# 중복 가능
# 같은 수열은 출력 X

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(range(1, N + 1))
seq = [0] * M

def perm(k):
    if k == M:
        print(*seq)
    else:
        for i in range(N):
            seq[k] = arr[i]
            perm(k + 1)

perm(0)