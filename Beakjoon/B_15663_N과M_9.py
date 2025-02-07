# 길이가 N인 리스트에서 M개를 고른 수열 출력
# 중복 X
# 리스트에 중복 숫자 존재
# 같은 수열은 출력 X

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M
visited = [0] * N

def perm(k):
    if k == M:
        print(*seq)
        return
    
    used = set()                                # 같은 depth에서 같은 숫자 중복 선택 방지
    for i in range(N):
        if visited[i] or arr[i] in used:        # 이미 선택했거나, 같은 depth에서 같은 숫자 선택 방지
            continue
        seq[k] = arr[i]
        visited[i] = 1
        used.add(arr[i])                        # 현재 depth에서 선택한 숫자 저장

        #-----------------------
        perm(k + 1)
        #-----------------------

        visited[i] = 0

perm(0)