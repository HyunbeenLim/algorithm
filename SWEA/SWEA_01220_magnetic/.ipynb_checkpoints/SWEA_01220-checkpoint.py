T = 10

for tc in range(1, T + 1):
    N = int(input()) # 100 고정
    board = [list(map(int, input().split())) for _ in range(N)]
    
    cnt = 0
    for c in range(N):
        r = 0
        stack = []
        while r < N:
            if board[r][c] == 1:
                stack.append(board[r][c])
            elif board[r][c] == 2 and stack:
                stack.pop()
                cnt += 1
                # 여러개가 겹쳐있어도 교착 상태는 하나로 센다
                stack = []
            r += 1
    print(f'#{tc} {cnt}')