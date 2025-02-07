import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

def perm(k):
    if k == M:
        print(*seq)
    else:
        for i in range(N):  
            if visited[i]: continue
            seq[k] = arr[i]
            visited[i] = 1
            #---------------------
            perm(k + 1)
            #---------------------
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    print(f'#{tc}')
    N, M = map(int, input().split())
    arr = list(range(1, N + 1))
    visited = [0] * N   # 요소 선택 여부 저장
    seq = [0] * M     # 실제 순열 저장

    perm(0)

# 제출용
# =======================================================
# import sys
# input = sys.stdin.readline

# def perm(k):
#     if k == M:
#         print(*seq)
#     else:
#         for i in range(N): 
#             if visited[i]: continue
#             seq[k] = arr[i]
#             visited[i] = 1
#             perm(k + 1)
#             visited[i] = 0

# N, M = map(int, input().split())
# arr = list(range(1, N + 1))
# visited = [0] * N
# seq = [0] * M
# perm(0)