import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# 공통 조상 찾는 함수
def find_common(node1, node2):
    q = deque()
    visited = [0] * (V + 1)

    q.append(node1)
    q.append(node2)

    while q:
        child = q.popleft()

        if graph[child][0] != 0:    # 이 조건 안 넣으면 0을 return하는 경우 발생
            if visited[graph[child][0]] != 0:   # 아래에서 위로 올라감
                return graph[child][0]          # 이미 방문했다 => 다른 노드의 조상이다 => 공통 조상이다
            else:
                visited[graph[child][0]] = 1
                q.append(graph[child][0])
    return

# 공통 조상 노드의 서브 트리 개수 구하는 함수
def count_nodes(node):
    q = deque()
    q.append(node)
    cnt = 1         # 공통 조상 노드도 노드 개수에 포함되어야 한다

    while q:
        parent = q.popleft()

        for child in graph[parent][1]:
            cnt += 1
            q.append(child)
    return cnt

for tc in range(1, int(input()) + 1):
    V, E, n1, n2 = map(int, input().split())

    graph = [[0, []] for _ in range(V + 1)]   # 인덱스 0: 해당 노드의 부모 노드, 인덱스 1: 해당 노드의 자식 노드들

    edges = list(map(int, input().split()))

    for i in range(2 * E):
        if i % 2 == 0:  # 부모 노드일 때
            graph[edges[i]][1].append(edges[i + 1]) # 해당 노드의 자식 저장
        else:   # 자식 노드일 때
            graph[edges[i]][0] = edges[i - 1]
    
    # 공통 조상
    common_anc = find_common(n1, n2)
    
    # 서브 트리 개수
    ans = count_nodes(common_anc)
    
    print(f'#{tc} {common_anc} {ans}')
    