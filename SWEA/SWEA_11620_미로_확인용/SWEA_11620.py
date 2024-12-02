import sys
sys.stdin = open('sample_input.txt', 'r', encoding='UTF-8')

def dfs(start):
    global visited
    
    stack = []
    stack.append(start)
    
    # 델타 우 하 좌 상
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    
    # 경로 탐색
    ## 스택이 비었으면 가능한 모든 경로를 찾은 것
    while stack:
        # 현재 반복에서 출발할 위치
        r, c = stack.pop()
        
        # 찾으면 1 반환
        if maze[r][c] == 3:
            return 1
        else:
            # 경로 탐색 시작
            ## 현재 위치 방문 기록
            visited[r][c] = 1
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                # 우 하 좌 상 인덱스 확인, 방문 기록 확인
                if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] != 1 and maze[nr][nc] != 1:
                    # 스택에 저장
                    stack.append((nr, nc))

    # 3을 못 찾았으면 0
    return 0
            


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    # 출발(2) 위치 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = i, j
    
    ans = dfs(start)
    
    print(f'#{tc} {ans}')
    
    


