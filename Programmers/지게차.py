from collections import deque

# 행렬 만들기
def make_matrix(lst):
    N = len(lst)
    M = len(lst[0])

    matrix = [[0] * (M+2) for _ in range(N+2)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            matrix[i][j] = lst[i-1][j-1]
    
    return {
        'matrix': matrix,
        'N': N,
        'M': M
    }

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 컨테이너 꺼내는 함수
def search(matrix, order, N, M):
    cnt = 0
    ## 길이가 1일 때 => 외부 접촉 컨테이너만
    if len(order) == 1:
        q = deque()
        visited = [[0] * (M+2) for _ in range(N+2)]

        q.append((0, 0))
        visited[0][0] = 1

        container_to_take = deque()         # 외부와 접촉된 컨테이너들

        while q:
            r, c = q.popleft()

            for m in range(4):
                nr = r + dr[m]
                nc = c + dc[m]
                if (0 <= nr < N + 2) and (0 <= nc < M + 2) and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if matrix[nr][nc] == order:
                        container_to_take.append((nr, nc))
                    elif matrix[nr][nc] == 0:
                        q.append((nr, nc))
        
        while container_to_take:
            r, c = container_to_take.popleft()
            matrix[r][c] = 0
            cnt += 1

        return {
            'matrix': matrix,
            'cnt': cnt
        }

    ## 길이 2일 때 => 모든 컨테이너
    else:
        for r in range(1, N+1):
            for c in range(1, M+1):
                if matrix[r][c] == order[0]:
                    matrix[r][c] = 0
                    cnt += 1

        return {
            'matrix': matrix,
            'cnt': cnt
        }


def solution(storage, requests):
    temp = make_matrix(storage)
    storage_matrix = temp['matrix']

    N = temp['N']
    M = temp['M']

    count = N * M

    for request in requests:
        take_container = search(storage_matrix, request, N, M)
        storage_matrix = take_container['matrix']
        count -= take_container['cnt']

    return count

solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])
solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"])

