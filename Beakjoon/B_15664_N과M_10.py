# 길이가 N인 리스트에서 M개를 고른 수열 출력
# 중복 X
# 리스트에 중복 숫자 존재
# 같은 수열은 출력 X
# 비내림차순

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N
seq = [0] * M

def perm(k):
    if k == M:
        print(*seq)
        return
    
    used = set()
    for i in range(N):
        if visited[i] or arr[i] in used:
            continue
        if k > 0 and seq[k-1] > arr[i]:
            continue
        seq[k] = arr[i]
        visited[i] = 1
        used.add(arr[i])

        perm(k + 1)

        visited[i] = 0

perm(0)