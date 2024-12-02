import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12398_그래프경로/sample_input.txt', 'r')


def dfs(s, l):
    visited = [0] * (l + 1)
    stack = []
    visited[s] = 1
    v = s
    while True:
        for w in g[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return visited

T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split()) # 정점, 간선
    g = [[] for _ in range(v + 1)] # 인접 리스트

    for _ in range(e):
        v1, v2 = map(int, input().split())
        g[v1].append(v2)

    start, end = map(int, input().split())
    visited = dfs(start, v)

    if visited[end]:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')


