############################################
##### 백트래킹만 한 것(시간 초과, 내가 짬) #####
############################################

def solution(info, n, m):
    ans = float("inf")
    max_depth = len(info) - 1

    def dfs(level, a_trace, b_trace):
        nonlocal ans
        # 체포
        if a_trace >= n or b_trace >= m:
            return
        
        # 이미 이전 최저값보다 높은 경우
        if a_trace >= ans:
            return
        
        # 끝 가지 도달
        if level == max_depth:
            if a_trace < n and b_trace < m:
                ans = min(ans, a_trace)
            return
        
        # 다음 물건
        dfs(level+1, a_trace+info[level+1][0], b_trace)
        dfs(level+1, a_trace, b_trace+info[level+1][1])
        
    dfs(0, info[0][0], 0)
    dfs(0, 0, info[0][1])

    return -1 if ans == float("inf") else ans

#########################
# 정답 코드(memoization) #
#########################

def solution(info, n, m):
    length = len(info)
    ans = float("inf")

    # visited[level][b_trace]
    # 같은 level, 같은 b_trace 값 중 최소 a_trace를 담아 둠
    visited = [[float("inf")] * m for _ in range(length + 1)]

    def dfs(level, a_trace, b_trace):
        nonlocal ans

        if a_trace >= n or b_trace >= m:
            return

        if a_trace >= ans:
            return

        # 같은 level, 같은 B 흔적에서
        # 이전보다 A 흔적이 많거나 같으면 열등한 경로
        if visited[level][b_trace] <= a_trace:
            return

        visited[level][b_trace] = a_trace

        if level == length:
            ans = a_trace
            return

        a, b = info[level]

        dfs(level + 1, a_trace, b_trace + b)
        dfs(level + 1, a_trace + a, b_trace)

    dfs(0, 0, 0)

    return -1 if ans == float("inf") else ans

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
print(solution([[3, 3], [3, 3]], 7, 1))
print(solution([[3, 3], [3, 3]], 6, 1))

