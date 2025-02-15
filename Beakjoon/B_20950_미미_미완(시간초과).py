import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def dfs(idx, curr_col, used_cnt):
    global min_diff

    if idx == N:            # N개 도달
        if used_cnt:
            diff = 0
            for i in range(3):
                curr_col[i] = int(curr_col[i]/used_cnt)
                diff += abs(curr_col[i] - goal[i])
            min_diff = min(diff, min_diff)
        return

    # 현재 색 선택
    for i in range(3):
        curr_col[i] = curr_col[i] + colors[idx][i]
    dfs(idx+1, curr_col, used_cnt+1)
    ## 백트래킹
    for i in range(3):
        curr_col[i] = curr_col[i] - colors[idx][i]

    # 현재 색 선택 X
    dfs(idx+1, curr_col, used_cnt)

N = int(input())

colors = []

for _ in range(N):
    colors.append(list(map(int, input().split())))

goal = list(map(int, input().split()))

min_diff = 1e10

dfs(0, [0,0,0], 0)

print(min_diff)