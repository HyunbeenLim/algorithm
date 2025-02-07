import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def perm(k):
    if k == M:
        print(*seq)
    else:
        for i in range(N):  
            if visited[i]: continue
            if k > 0 and seq[k-1] > arr[i]:
                continue
            seq[k] = arr[i]
            visited[i] = 1
            #---------------------
            perm(k + 1)
            #---------------------
            visited[i] = 0


N, M = map(int, input().split())
arr = list(range(1, N + 1))
visited = [0] * N
seq = [0] * M
perm(0)

