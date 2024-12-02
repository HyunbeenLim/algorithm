T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    
    # 최대 낙하
    max_fall = 0
    for i in range(N - 1): # 맨 아래층 제외
        # i 번째 층 가장 위 블럭 아래 깔리는 블럭 수
        below_boxes = 0
        for j in range(i + 1, N): # i + 1부터 마지막 층까지 확인
            if boxes[i] <= boxes[j]: # j번째 층이 더 길면 i번째 층의 맨 위 박스가 내려갈 거리가 1 줄어들게 됨
                below_boxes += 1
        # 떨어지는 거리 = N - i - 아래 깔리는 박스들  - 1
        distance_to_fall = (N - i) - below_boxes - 1 
        # 최대 낙하 거리 갱신
        if max_fall < distance_to_fall:
            max_fall = distance_to_fall
        # 남은 층보다 max_fall이 더 크면 반복 종료
        if max_fall > (N - i):
            break
    
    print(f'#{tc} {max_fall}')
        