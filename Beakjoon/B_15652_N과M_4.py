# 중복 가능
# 비내림차순 -> a1 <= a2

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
            if k > 0 and seq[k-1] > arr[i]:
                continue
            seq[k] = arr[i]
            perm(k + 1)

perm(0)