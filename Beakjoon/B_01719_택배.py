import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
INF = 1e9
dist = [[INF] * (N+1) for _ in range(N+1)]
route = [[0] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dist[i][i] = 0
    route[i][i] = '-'

for _ in range(M):
    v1, v2, w = map(int, input().split())
    dist[v1][v2] = w
    dist[v2][v1] = w
    route[v1][v2] = v2
    route[v2][v1] = v1

# 플로이드 워셜
for k in range(1, N+1):                                 # 중간 지점 k를 하나씩 선택하여 모든 경로를 개선
    for i in range(1, N+1):                             # 출발점 i에서
        for j in range(1, N+1):                         # 도착점 j로 가는 경로를 점검
            if dist[i][j] > dist[i][k] + dist[k][j]:    # 기존 i→j보다 i→k→j가 더 짧다면,
                dist[i][j] = dist[i][k] + dist[k][j]    # 최단 경로 길이를 갱신
                route[i][j] = route[i][k]               # i에서 j로 갈 때 최초로 거쳐야 하는 집하장을 기록

print_route = [[0] * N for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, N+1):
        print_route[i-1][j-1] = str(route[i][j])

for frac in print_route:
    print(' '.join(frac))