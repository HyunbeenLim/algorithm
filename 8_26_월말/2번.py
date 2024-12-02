# 위험도 계산 함수
def calculate(start):
    stack = []
    # 이전에 방문했던 row 값은 col 값으로 사용될 수 없으므로 visited 만들기
    visited = [0] * N
    stack.append(start)
    r, c = start
    visited[r] = 1
    # 위험도
    sum_value = matrix[r][c]

    while stack:
        r, c = stack.pop()
        # 외계인이 줄을 서기 때문에 이전의 col 값은 다음의 row 값으로 사용됨
        new_r = c

        # 탐색 가능한 위치의 위험도 다 넣기
        temp_elements = []
        for new_c in range(N):
            # 현재 탐색하고자 하는 위치의 col 값이 이전에 방문한 row 값이 아닌지 확인
            # 아니라면 temp 리스트에 넣기
            if matrix[new_r][new_c] != 0 and visited[new_c] != 1:
                # 해당 위치의 위험도 값과 col 값 저장
                temp_elements.append([matrix[new_r][new_c], new_c])
        
        # temp 리스트가 비어있으면 이전 new_r, new_c 값을 재활용하기 때문에 무한 루프를 돌게 된다
        # 비어있지 않을 때만 append 하게 조건을 걸기
        if temp_elements:
            min_ele = float('inf')
            new_c = 0
            # temp 리스트 중 최솟값을 찾아 더해주고 col 값을 new_c로 저장
            for arr in temp_elements:
                if arr[0] < min_ele:
                    min_ele = arr[0]
                    new_c = arr[1]
            sum_value += min_ele
            # visit
            visited[new_r] = 1
            # push
            stack.append((new_r, new_c))

    return sum_value

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 가능한 모든 경우의수 고려하여 최솟값 찾기
    min_value = float('inf')
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                curr_value = calculate((r, c))
                if curr_value < min_value:
                    min_value = curr_value

    print(f'#{tc} {min_value}')
