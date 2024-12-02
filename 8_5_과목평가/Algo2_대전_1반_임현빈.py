# 문제 2 완만한 오르막
## 높이 차이가 0인 애들 지우는 로직 없어서 틀림! 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    path = list(map(int, input().split()))
    # 각 오르막길이 끝나는 지점
    path_end = []
    for i in range(N - 1):
        if path[i] > path[i + 1]:
            path_end.append(i)
    path_end.append(N - 1)
    # 오르막길 개수
    path_number = len(path_end)

    # 초기 최소 경사도
    min_degree = float('inf')
    # 최소 경사도 일때 길이
    length = 0
    # while 문 내에서 등산로 가져오기 위한 오르막길 시작 인덱스
    start_idx = 0
    # 등산로 끝 지점을 인덱스로 가져오는 역할과 while 문 종료 역할
    cnt = 0
    while cnt <= (path_number - 1):
        # 끝나는 지점 가져오기
        path_endpoint = path_end[cnt]
        path_i = path[start_idx:(path_endpoint + 1)]
        start_idx = (path_endpoint + 1)
        cnt += 1
        # 길이
        path_length = len(path_i)
        # 오르막길 길이가 2 미만이면 다음 반복으로
        if path_length < 2:
            continue
        else:
            # 경사도
            degree = (path_i[path_length - 1] - path_i[0]) / path_length
            # 일단 최소 경사면, 길이와 경사도 저장
            if min_degree > degree:
                min_degree = degree
                length = path_length
            # 최소 경사도와 같은 경사도를 가진다면, 더 긴 길이 저장
            elif min_degree == degree:
                if length < path_length:
                    length = path_length

    print(f'#{tc} {length}')