import sys
sys.stdin = open('sample_input.txt', 'r')

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 블럭에 부딪힌 뒤 바뀌는 방향
blocks = [
    [],
    [2, 0, 3, 1], 
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [3, 2, 0, 1],
    [2, 3, 0, 1]
]

# 웜홀 짝 찾기
def find_wormhole(matrix):
    wormhole = [[] for _ in range(5)]

    for r in range(N):
        for c in range(N):
            if matrix[r][c] in [6, 7, 8, 9, 10]:
                wormhole[matrix[r][c] - 6].append((r, c))
    return wormhole
        
# 코드 깔끔하게
def game_play(start_r, start_c, wormhole, start_direction):
    global max_score
    
    score = 0
    current_r = start_r
    current_c = start_c
    current_direction = start_direction
    
    while True:
        nr = current_r + dr[current_direction]
        nc = current_c + dc[current_direction]
        
        # 인덱스를 벗어나는 순간 벽에 부딪힌 것으로 판정, 점수 올리고 방향만 바꿔주기
        if not (0 <= nr < N) or not (0 <= nc < N):
            score += 1
            current_direction = (current_direction + 2) % 4
            
            # 벽에 부딪히면 field 탐색 X => 인덱스를 벗어난 상태의 좌표를 현재 위치로 지정해줘도 괜찮음
            # 방향이 바뀌기 때문에 다음 nr, nc는 무조건 field 안의 좌표
            current_r, current_c = nr, nc
        # nr, nc가 field 안의 좌표일 때
        else:
            value = field[nr][nc]
            current_r, current_c = nr, nc
            # 게임 종료 규칙
            if value == -1 or (current_r, current_c) == (start_r, start_c):
                break
            # 블럭 만났을 때
            elif value in [1, 2, 3, 4, 5]:
                # 점수 올리기
                score += 1
                # 방향 바꾸기
                current_direction = blocks[value][current_direction]
            # 웜홀
            elif value in [6, 7, 8, 9, 10]:
                pairs =  wormhole[value - 6]
                # 웜홀은 번호당 한쌍만 존재, 현재 좌표와 다른 좌표가 이동할 웜홀의 좌표
                for position in pairs:
                    if (current_r, current_c) != position:
                        current_r, current_c = position
                        break
    if max_score < score:
        max_score = score

for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀 리스트
    wormholes = find_wormhole(field)
    
    max_score = -1

    for r in range(N):
        for c in range(N):
            if field[r][c] == 0:
                for direction in range(4):
                    game_play(r, c, wormholes, direction)

    print(f'#{tc} {max_score}')