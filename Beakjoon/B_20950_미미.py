import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def dfs(idx, cur_R, cur_G, cur_B, used_cnt):
    global min_diff

    if used_cnt == 7:
        diff = abs(int(cur_R/used_cnt) - goal[0]) + abs(int(cur_G/used_cnt) - goal[1]) + abs(int(cur_B/used_cnt) - goal[2])
        min_diff = min(diff, min_diff)
        return

    if idx == N:            # N개 도달
        if used_cnt > 1:
            diff = abs(int(cur_R/used_cnt) - goal[0]) + abs(int(cur_G/used_cnt) - goal[1]) + abs(int(cur_B/used_cnt) - goal[2])
            min_diff = min(diff, min_diff)
        return

    # 현재 색 선택
    dfs(idx+1, cur_R+R[idx], cur_G+G[idx], cur_B+B[idx], used_cnt+1)

    # 현재 색 선택 X
    dfs(idx+1, cur_R, cur_G, cur_B, used_cnt)

N = int(input())

R = []
G = []
B = []

for _ in range(N):
    color = list(map(int, input().split()))
    R.append(color[0])
    G.append(color[1])
    B.append(color[2])

goal = list(map(int, input().split()))

min_diff = 255 * 3 + 1

dfs(0, 0, 0, 0, 0)

print(min_diff)