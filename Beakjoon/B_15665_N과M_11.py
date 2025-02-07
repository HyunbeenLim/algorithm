# 길이가 N인 리스트에서 M개를 고른 수열 출력
# 중복 가능
# 리스트에 중복 숫자 존재
# 같은 수열은 출력 X

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
seq = [0] * M

def perm(k):
    if k == M:
        print(*seq)
        return
    
    used = set()
    for i in range(N):
        if arr[i] in used:
            continue
        seq[k] = arr[i]
        used.add(arr[i])
        
        perm(k + 1)

perm(0)