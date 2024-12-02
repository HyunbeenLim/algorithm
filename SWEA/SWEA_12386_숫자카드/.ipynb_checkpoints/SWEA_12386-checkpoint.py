T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input()))
    
    # 빈도 리스트
    count_list = [0] * 10
    for card in cards:
        count_list[card] += 1
        
    # 최빈값
    mode = 0
    # 최빈값 인덱스
    max_idx = 0
    # 최빈값, 인덱스 업데이트
    for i in range(len(count_list)):
        freq_i = count_list[i]
        if freq_i >= mode:
            mode = freq_i
            max_idx = i
    
    print(f'#{tc} {max_idx} {mode}')