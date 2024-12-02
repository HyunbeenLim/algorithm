import sys
sys.stdin = open('sample_input.txt', 'r')

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 시작 지점
def find_start():
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                return (r, c)

# 마지막 지점
def find_goal():
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'Y':
                return (r, c)

def manipulate(string, start):
    global direction

    r, c = start

    for order in string:
        if order == 'R':
            direction += 1
            direction %= 4
        elif order == 'L':
            direction -= 1
            direction %= 4
        else:
            nr = r + dr[direction]
            nc = c + dc[direction]
            if (0 <= nr < N) and (0 <= nc < N) and field[nr][nc] != 'T':
                r = nr
                c = nc
    
    return (r, c)


for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(input()) for _ in range(N)]

    start = find_start()
    goal = find_goal()

    ans_list = []
    M = int(input())

    for _ in range(M):
        direction = 3
        
        num, orders = input().split()

        temp_i = manipulate(orders, start)
        if temp_i == goal:
            ans_list.append(1)
        else:
            ans_list.append(0)
    
    print(f'#{tc}', *ans_list)