import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import deque

# bfs
def bfs():
    global graph

    order = []
    q = deque()
    visited = [0] * (V + 1)

    for node in range(1, V + 1):    # 진입 차수가 0이고, 방문한적이 없다면
        if graph[node][0] == 0:
            q.append(node)
            visited[node] = 1

    while q:
        # 작업 순서에 넣고
        node = q.popleft()
        order.append(node)

        for child in graph[node][1]:
            graph[child][0] -= 1    # 연결된 간선 다 지우기
            if graph[child][0] == 0 and visited[child] == 0:
                q.append(child)
                visited[child] = 0
        
    return order

for tc in range(1, 11):
    V, E = map(int, input().split())

    graph = [[0, []] for _ in range(V + 1)] # 진입 차수, 자식 노드 리스트

    edges = list(map(int, input().split()))

    for i in range(2 * E):
        if i % 2 == 0:  
            graph[edges[i]][1].append(edges[i + 1]) # 부모일 때 -> 해당 노드의 자식 저장
        else:
            graph[edges[i]][0] += 1             # 자식일 때 -> 진입 차수 올려주기

    ans = bfs()
    
    print(f'#{tc}', end = ' ')
    for node in ans:
        print(node, end = ' ')
    print()

    