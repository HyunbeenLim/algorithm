import sys
input = sys.stdin.readline

N = int(input())
arr = list(range(1, N + 1))
visited = [0] * N
seq = [0] * N

def perm(idx):
    if idx == N:
        print(*seq)
        return
    for i in range(N):
        if visited[i]:
            continue
        seq[idx] = arr[i]
        visited[i] = 1
        perm(idx+1)
        visited[i] = 0

perm(0)