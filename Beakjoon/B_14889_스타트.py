import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, team_1, team_2):
    global min_diff
    
    if idx == N:
        if len(team_1) == N // 2:
            s1 = 0
            s2 = 0
            for i in range(N//2):
                for j in range(N//2):
                    s1 += S[team_1[i]][team_1[j]]
                    s2 += S[team_2[i]][team_2[j]]

            diff = abs(s1 - s2)
            min_diff = min(diff, min_diff)
        return
    
    if len(team_1) > N // 2:
        return
            
    dfs(idx+1, team_1+[idx], team_2)
    dfs(idx+1, team_1, team_2+[idx])

for tc in range(1, int(input()) + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    min_diff = N * N * 100

    dfs(0, [], [])

    print(f'#{tc} {min_diff}')



######## 제출용 ########
# import sys
# input = sys.stdin.readline

# def dfs(idx, team_1, team_2):
#     global min_diff
    
#     if idx == N:
#         if len(team_1) == N // 2:
#             s1 = 0
#             s2 = 0
#             for i in range(N//2):
#                 for j in range(N//2):
#                     s1 += S[team_1[i]][team_1[j]]
#                     s2 += S[team_2[i]][team_2[j]]

#             diff = abs(s1 - s2)
#             min_diff = min(diff, min_diff)
#         return
            
#     dfs(idx+1, team_1+[idx], team_2)
#     dfs(idx+1, team_1, team_2+[idx])

# N = int(input())
# S = [list(map(int, input().split())) for _ in range(N)]

# min_diff = N * N * 100

# dfs(0, [], [])

# print(min_diff)