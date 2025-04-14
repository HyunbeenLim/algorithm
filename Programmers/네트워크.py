from collections import deque

def solution(n, computers):
    # 연결 여부 확인
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)

    # 네트워크 개수 세기
    cnt = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                parent = q.popleft()

                for child in graph[parent]:
                    if not visited[child]:
                        visited[child] = 1
                        q.append(child)
            cnt += 1
    
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(1,[[1]]))
print(solution(3,[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(solution(4,[[1, 1, 0, 0],[1, 1, 0, 0],[0, 0, 1, 1],[0, 0, 1, 1]])) # 2
print(solution(4,[[1, 1, 0, 0],[1, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])) # 3
print(solution(2,[[1, 1],[1, 1]])) # 1
