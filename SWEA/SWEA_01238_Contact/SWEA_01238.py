import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_01238_Contact/input.txt', 'r')

def bfs(start):
    global q
    visited = [0] * 101
    visited[start] = 1
    q.append(start)
    while q:
        v = q.popleft()
        for w in G[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    return visited

from collections import deque

for tc in range(1, 11):
    N, start = map(int, input().split())
    q = deque()

    # 인접 리스트
    arrows = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(0, N, 2):
        v1, v2 = arrows[i], arrows[i + 1]
        if v2 not in G[v1]:
            G[v1].append(v2)

    visited = bfs(start)

    idx = 0
    count = 0
    for i in range(101):
        if visited[i] >= count:
            count = visited[i]
            idx = i

    print(f'#{tc} {idx}')