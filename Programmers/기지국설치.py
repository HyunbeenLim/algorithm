# def solution(n, stations, w):
#     # 현재 전파가 닿는 곳 표시
#     apts = [0] * (n + 1)
#     for st in stations:
#         left = max(1, st-w)
#         right = min(n, st+w)
#         for i in range(left, right+1):
#             apts[i] = 1

#     # 설치할 기지국 찾기
#     installed = 0
#     idx = 1
#     while idx < n+1:
#         if apts[idx] == 0:
#             installed_pos = min(n, idx+w)
#             installed += 1

#             # 전파 가능 범위
#             left = max(1, installed_pos-w)
#             right = min(n, installed_pos+w)
#             for i in range(left, right+1):
#                 if apts[i] == 0:
#                     apts[i] = 1
#                 # 가다가 이미 전파가 닿는 곳이 있다면 이전 칸에 기지국 설치
#                 else:
#                     right = i-1
#             idx = right + 1

#         else:
#             idx += 1
        
#     return installed

import math

def solution(n, stations, w):
    coverage = 2 * w + 1
    answer = 0
    start = 1

    for station in stations:
        left = station - w
        right = station + w

        # 전파가 닿지 않는 구간이 있다면
        if start < left:
            gap = left - start
            answer += math.ceil(gap / coverage)

        # 다음 시작점 갱신
        start = right + 1

    # 마지막 기지국 이후에도 커버 안 된 곳이 있다면
    if start <= n:
        gap = n - start + 1
        answer += math.ceil(gap / coverage)

    return answer

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))