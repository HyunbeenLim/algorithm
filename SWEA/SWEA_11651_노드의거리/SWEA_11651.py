import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_11651_노드의거리/sample_input.txt', 'r')

from collections import deque

def bfs(start, end):
    global q
    visited = [0] * (V + 1)
    visited[start] = 1
    q.append(start)
    while q:
        v = q.popleft()
        for w in G[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
                if w == end:
                    return visited[end] - 1
    return 0


T = int(input())

for tc in range(1, T + 1):
    q = deque()
    V, E = map(int, input().split())

    # 인접 리스트
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)

    start, end = map(int, input().split())

    ans = bfs(start, end)

    print(f'#{tc} {ans}')




