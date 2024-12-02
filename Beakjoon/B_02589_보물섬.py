import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    q = deque()
    r, c = start
    q.append((r, c))
    # 숫자 올려주는 매트릭스, visited 개념
    hours = [[0] * M for _ in range(N)]
    hours[r][c] = 1
    
    current_hours = 0
    while q:
        r, c = q.popleft()
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if (0 <= nr < N) and (0 <= nc < M) and treasure_map[nr][nc] == 'L' and hours[nr][nc] == 0:
                # 이동할 때마다 시간 더해주기
                hours[nr][nc] = hours[r][c] + 1
                # 현재 이동 시간
                current_hours = hours[nr][nc]
                q.append((nr, nc))
                
    # 첫 시작 값 빼준 것 return
    return current_hours - 1
    

N, M = map(int, input().split())

treasure_map = [list(input().strip()) for _ in range(N)]

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

max_hours = -1
for r in range(N):
    for c in range(M):
        if treasure_map[r][c] == 'L':
            temp_hours = bfs((r, c))
            if max_hours < temp_hours:
                max_hours = temp_hours

print(max_hours)