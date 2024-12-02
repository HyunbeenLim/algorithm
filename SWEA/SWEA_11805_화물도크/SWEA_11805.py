import sys
sys.stdin = open('./sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cars = []

    for _ in range(N):
        cars.append(list(map(int, input().split())))

    # 끝나는 시간 기준 정렬
    cars.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end = 0
    for schedule in cars:
        start = schedule[0]
        if start >= end:
            cnt += 1
            end = schedule[1]

    print(f'#{tc} {cnt}')