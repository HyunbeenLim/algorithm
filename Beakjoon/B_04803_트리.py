import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

from collections import deque
import copy

case = 1
while True:
    nodes, edges = map(int, input().split())

    if nodes == 0 and edges == 0:
        break
    
    graph = []

    for _ in range(nodes+1):
        graph.append([0, []])
    
    for _ in range(edges):
        v1, v2 = map(int, input().split())

        # 부모가 있는 노드의 진입 차수
        graph[v2][0] += 1

        # 자식 노드
        graph[v1][1].append(v2)

    tree_cnt = 0
    
    for i in range(1, nodes+1):
        # 진입 차수가 0일 때
        if graph[i][0] == 0:
            # 자식 노드가 없을 때 -> 그 자체로 트리
            if not graph[i][1]:
                tree_cnt += 1
            else:
                temp_graph = copy.deepcopy(graph)
                visited = [0] * (nodes+1)
                visited[i] = 1
                
                q = deque()
                q.append(i)

                while q:
                    parent = q.popleft()

                    for child in temp_graph[parent][1]:
                        if visited[child]:
                            break
                        
                        idx = temp_graph[parent][1].index(child)
                        temp_graph[parent][1].pop(idx)
                        temp_graph[child][0] -= 1

                        if temp_graph[child][0] == 0:
                            visited[child] = 1
                            q.append(child)
                else:
                    tree_cnt += 1

    if tree_cnt == 0:
        ans = 'No trees.'
    elif tree_cnt == 1:
        ans = 'There is one tree.'
    else:
        ans = f'A forest of {tree_cnt} trees'

    print(f'Case {case}: {ans}')
    case += 1