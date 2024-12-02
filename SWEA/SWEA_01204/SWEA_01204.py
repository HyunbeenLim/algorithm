T = int(input())

for tc in range(1, T + 1):
    useless = int(input())
    scores = list(map(int, input().split()))
    
    # 인덱스가 점수 그 자체를 나타내게
    count_list = [0] * 101
    
    for score in scores:
        count_list[score] += 1
    
    # 최빈값
    mode = 0
    # 최빈값 인덱스(가장 많은 점수)
    freq_idx = 0
    for i in range(len(count_list)):
        # 점수 별 빈도 수
        freq = count_list[i]
        # 최빈값, 최빈값 인덱스 업데이트, =을 붙여줘야 같은 빈도일 때 높은 인덱스로 업데이트
        if freq >= mode:
            mode = freq
            freq_idx = i
        
    print(f'#{tc} {freq_idx}')