import sys
input = sys.stdin.readline

def dfs(day, weight):
    global cnt

    if weight < 500:
        return
    
    if day == N:
        cnt += 1
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(day+1, weight+kits[i]-K)
            visited[i]=0

N, K = map(int, input().split())
kits = list(map(int, input().split()))
visited = [0] * N
cnt = 0

dfs(0, 500)

print(cnt)