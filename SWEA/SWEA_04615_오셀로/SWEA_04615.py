T = int(input())

# 오른쪽부터 시계 방향으로 8 방향
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def stone_count(r, c, color):
    global board
    
    # 사이에 놓인 돌의 색 확인
    if color == 1:
        color_to_count = 2
    elif color == 2:
        color_to_count = 1
    
    cnt = 0
    # 8방향 다 돌기
    for k in range(8):
        # 원래 색을 만나야 돌을 뒤집고, cnt를 올려줄 수 있다.
        temp_cnt = 0
        validity = False
        for m in range(1, N):
            nr = r + m * dr[k]
            nc = c + m * dc[k]
            # 인덱스 확인
            if (0 <= nr < N) and (0 <= nc < N):
                # 찾을 색과 같다면 count 올려주고 색 바꾸기
                if board[nr][nc] == color_to_count:
                    temp_cnt += 1
                elif board[nr][nc] == color:
                    validity = True
                    break
                # 0이면 바로 멈추기
                else:
                    break
            # 인덱스 넘어가면 바로 멈춰주기
            else: break
        # validity True라면 만났던 상대 돌들 뒤집고 cnt 올리기
        if validity:
            for m in range(1, temp_cnt + 1):
                nr = r + m * dr[k]
                nc = c + m * dc[k]
                board[nr][nc] = color
            cnt += temp_cnt
    # 8방향 모두 count
    return cnt
            
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    
    # 기본
    # 1 - black, 2 - white
    idx = N // 2
    
    board[idx-1][idx-1] = 2
    board[idx-1][idx] = 1
    board[idx][idx] = 2
    board[idx][idx-1] = 1
    
    white_cnt = 2
    black_cnt = 2
    
    for _ in range(M):
        c, r, color = map(int, input().split()) # 행, 열 좌표 반대로 input됨
        board[r-1][c-1] = color
        
        # 뒤집을 돌의 개수
        changed_stones = stone_count(r-1, c-1, color)
        
        # 돌을 두면서 하나가 늘어났기 때문에 +1
        if color == 1:
            black_cnt = black_cnt + 1 + changed_stones
            white_cnt = white_cnt - changed_stones
        elif color == 2:
            white_cnt = white_cnt + 1 + changed_stones
            black_cnt = black_cnt - changed_stones
            
    print(f'#{tc} {black_cnt} {white_cnt}')
    
    

    
# ===============================================
## 교수님 코드
def osello(x, y, col, N):
    # 일단 인풋 받은대로 돌을 놓고
    board[x][y] = col
    # 위아래에 직선으로 돌을 탐색하면서
    # 경우1) 선 끝에 자신이랑 같은 돌이 있으면, 자기랑 같은 색의 돌을 만날때까지 반대 색 뒤집어줌
    # 경우2) 선 끝에 자신이랑 같은 돌이 없으면, 그냥 놓고 끝

    delta = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,0], [0,1], [1,-1], [1,0], [1,1]]
    op = [0, 2, 1] # 반대돌의 값을 인덱스로 불러오는 리스트
    # 돌을 놓은 x,y 지점부터 모든 방향의 델타를 확인함
    for di, dj in delta:
        ni = x + di
        nj = y + dj
        tmp = []
        # 범위안에 있고, 자기랑 다른 값을 가지는 한 반복 (즉, 자기랑 같은 색을 만나면 멈춤)
        while 0<=ni<N and 0<=nj<N and board[ni][nj] == op[col]:
            tmp.append([ni, nj])
            ni, nj = ni+di, nj+dj # 현재방향으로 일단 계속 이동하면서 탐색해야함.
        # 이걸 if 문에 안넣으면 탐색한 모든 값이 그냥 바뀌는 결과
        # 따라서 자기랑 다른 값을 가질때만 색을 바꾼다는 조건을 걸어야함.
        if 0<=ni<N and 0<=nj<N and board[ni][nj] == col:
            for a, b in tmp:
                board[a][b] = col #tmp에 모였던 애들은 본인의 색으로 바꿔줌




# 우선 인풋부터 받아보자
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 보드 길이, M : 돌 놓는 횟수
    board = [[0] * N for _ in range(N)] # N* N 행렬의 보드 만들기

    B = 1
    W = 2

    # 초기 보드 세팅
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W


    for i in range(M): # 돌 놓는 횟수만큼 어디 놓을지 받기
        x, y, col = map(int, input().split())
        osello(x-1, y-1, col, N) #입력 순서 주의!! 문제에서 돌을 놓는 col, row 는 1부터 시작

    # 전부 끝난 뒤에 색깔 카운트
    cnt_B = 0
    cnt_W = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == B:
                cnt_B += 1
            elif board[r][c] == W:
                cnt_W += 1
    print(f'#{tc} {cnt_B} {cnt_W}')
