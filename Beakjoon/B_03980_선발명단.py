import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

def dfs(idx, value):
    global max_stat, visited

    if idx == N:
        max_stat = max(max_stat, value)
        return

    for i in range(N):
        # 방문하지 않았고, 0이 아닌 스탯만 확인
        if not visited[i] and stats[idx][i]:
            visited[i] = 1
            dfs(idx+1, value+stats[idx][i])
            visited[i] = 0

for _ in range(int(input())):
    N = 11
    stats = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    max_stat = -1

    dfs(0, 0)

    print(max_stat)