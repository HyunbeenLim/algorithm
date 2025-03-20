from collections import deque

def make_graph(n, edges):
    graph = [[] for _ in range(n+1)]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

def bfs(n, graph):
    q = deque()

    visited = [0] * (n+1)
    visited[1] = 1

    for child in graph[1]:
        visited[child] = 1
        q.append(child)
    
    max_dist = 0

    while q:
        parent = q.popleft()

        for child in graph[parent]:
            if not visited[child]:
                visited[child] = visited[parent] + 1
                if visited[child] > max_dist:
                    max_dist = visited[child]
                q.append(child)

    return [visited, max_dist]


def solution(n, edges):
    graph = make_graph(n, edges)

    tracking = bfs(n, graph)

    visited = tracking[0]
    max_dist = tracking[1]

    cnt = 0

    for dist in visited:
        if dist == max_dist:
            cnt += 1

    return cnt



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))