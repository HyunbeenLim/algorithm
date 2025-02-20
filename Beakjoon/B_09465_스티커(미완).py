import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

####### dp 도전 #######

for _ in range(int(input())):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    for i in range(2):
        dp[i][0] = stickers[i][0]
    
    if N == 2:
        for j in range(1, N):
            dp[0][j] = dp[1][j-1] + stickers[0][j]
            dp[1][j] = dp[0][j-1] + stickers[1][j]
    elif N >= 3:
        for j in range(1, N-2):
            dp[0][j] = dp[1][j-1] + stickers[0][j]
            dp[1][j] = dp[0][j-1] + stickers[1][j]
        
        dp[0][N-1] = max(dp[0][N-3]+stickers[1][N-2]+stickers[0][N-1], dp[1][N-3]+stickers[0][N-1])
        dp[1][N-1] = max(dp[1][N-3]+ stickers[0][N-2]+stickers[1][N-1], dp[0][N-3]+stickers[1][N-1])
    
    # print('---')
    # for frac in dp:
    #     print(frac)
    print(max(dp[0][N-1], dp[1][N-1]))


    


####### dp 안 쓴 풀이(시간초과) #######

# # 제자리, 우 하 좌 상
# dr = [0, 0, 1, 0, -1]
# dc = [0, 1, 0, -1, 0]

# for _ in range(int(input())):
#     N = int(input())
#     stickers = [list(map(int, input().split())) for _ in range(2)]

#     total_score = 0
    
#     while True:
#         zero_cnt = 0
#         max_score = 0

#         for i in range(2):
#             for j in range(N):
#                 if stickers[i][j] == 0:
#                     zero_cnt += 1
#                 elif stickers[i][j] > max_score:
#                     max_score = stickers[i][j]
#                     max_pos = (i, j)
        
#         if zero_cnt == 2 * N:
#             print(total_score)
#             break
        
#         r, c = max_pos
#         total_score += stickers[r][c]
        
#         # 인접 요소 0
#         for k in range(5):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if (0 <= nr < 2) and (0 <= nc < N) and stickers[nr][nc]:
#                 stickers[nr][nc] = 0