import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_01873_상호의배틀필드/input.txt', 'r')

T = int(input())

# 처음 탱크 위치 찾기
def search_tank():
    for h in range(H):
        for w in range(W):
            for k in range(4):
                if direction[k] == field[h][w]:
                    location = h, w
                    heading_to = k
                    # 탱크 위치와 바라보는 방향
                    return {
                        'location': location,
                        'heading_to': heading_to
                    }
                
    return print('Cannot find the tank in the field')
    

def manipulate(order, location, heading_to):
    global field
    current_r = location[0]
    current_c = location[1]
    
    # 포탄 발사!
    # 포탄 발사 명령 -> 탱크 위치 변환 X
    if order == 'S':
        for m in range(1, max_idx):
            # 포탄이 날아갈 방향
            nr = current_r + m * dr[heading_to]
            nc = current_c + m * dc[heading_to]
            
            if (0 <= nr < H) and (0 <= nc < W):
                # 유효한 인덱스 안에서 벽을 만났을 때
                if field[nr][nc] == '*':
                    field[nr][nc] = '.'
                    break
                elif field[nr][nc] == '#':
                    break
            # 인덱스 넘어가면 포탄은 그냥 없어짐
            else:
                break
    # 방향이 주어졌을 때
    else:
        # 이동하는 순간 바라보는 곳은 변한다
        heading_to = order
        next_r = current_r + dr[heading_to]
        next_c = current_c + dc[heading_to]
        # 이동 가능한 방향이라면 가자
        if (0 <= next_r < H and 0 <= next_c < W):
            if field[next_r][next_c] == '.':
                field[current_r][current_c] = '.'
                field[next_r][next_c] = direction[heading_to]
                location = next_r, next_c
            else:
                field[current_r][current_c] = direction[heading_to]
        else:
            field[current_r][current_c] = direction[heading_to]
    
    return {
        'field': field,
        'location': location,
        'heading_to': heading_to
    }

for tc in range(1, T + 1):
    H, W = map(int, input().split())              # 높이, 너비
    if H > W:
        max_idx = H
    else:
        max_idx = W
    
    field = [list(input()) for _ in range(H)]     # H x W matrix

    direction = '>v<^'
    
    search = search_tank()
    heading_to = search['heading_to']
    location = search['location']
    
    N = int(input())
    orders = input()

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    for order in orders:
        # 방향 인덱스
        if order == 'R':
            order = 0
        elif order == 'D':
            order = 1
        elif order == 'L':
            order = 2
        elif order == 'U':
            order = 3
        
        game_play = manipulate(order = order, location = location, heading_to = heading_to)
        field = game_play['field']
        location = game_play['location']
        heading_to = game_play['heading_to']
    
    first_row = field[0]
    print(f'#{tc}', end = ' ')
    for w in range(W):
        print(first_row[w], end = '')
    print()
    for h in range(1, H):
        arr = field[h]
        for w in range(W):
            print(arr[w], end = '')
        print()