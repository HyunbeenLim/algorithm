import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
field = [[0] * W for _ in range(H)]

blocks = list(map(int, input().split()))

for c in range(W):
    block_cnt = blocks[c]
    for r in range(H-1, H-block_cnt-1, -1):
        field[r][c] = 1

cnt = 0     # 고인 빗물

for r in range(H):
    c = 0
    # 처음 블럭을 만날 때까지 고일 빗물을 세지 않기
    to_count = False
    while c < W:
        # 블럭을 처음 만났을 때부터 고일 빗물 세기
        if field[r][c] == 1 and not to_count:
            temp_cnt = 0
            to_count = True
        elif field[r][c] == 0 and to_count:
            temp_cnt += 1
        # 고일 빗물을 세고 있을 때 블럭을 만났으면, 고인다는 의미 -> 답 cnt에 더해주기
        elif field[r][c] == 1 and to_count and temp_cnt > 0:
            cnt += temp_cnt
            temp_cnt = 0
        c += 1

print(cnt)