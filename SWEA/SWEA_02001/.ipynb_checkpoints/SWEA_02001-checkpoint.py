import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_02001/input.txt", "r")
# input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    N, M = map(int, input().split())

    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = int()
    count = int()

    if N == M:
        max_fly = sum(list(map(sum, fly_arr)))
        print(max_fly)
    else:
        for i in range(N - M + 1):
            for j in range(N - M + 1):
                count = 0
                for u in range(i, i + M):
                    for v in range(j, j + M):
                        count += fly_arr[u][v]
                if max_fly < count:
                    max_fly = count

        print(max_fly)