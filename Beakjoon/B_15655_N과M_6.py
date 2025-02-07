# 길이가 N인 리스트에서 M개를 고른 수열 출력
# 중복 X
# 오름차순

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N
seq = [0] * M

def perm(k):
    if k == M:
        print(*seq)
    else:
        for i in range(N):
            if visited[i]:
                continue
            if k > 0 and seq[k-1] > arr[i]:
                continue
            seq[k] = arr[i]
            visited[i] = 1
            perm(k + 1)
            visited[i] = 0

perm(0)
