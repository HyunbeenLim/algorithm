#### 첫번째

# T = int(input())

# for tc in range(1, T + 1):
#     n = int(input())
#     cards = list(map(int, input()))
    
#     # 빈도 리스트
#     count_list = [0] * 10
#     for card in cards:
#         count_list[card] += 1
        
#     # 최빈값
#     mode = 0
#     # 최빈값 인덱스
#     max_idx = 0
#     # 최빈값, 인덱스 업데이트
#     for i in range(len(count_list)):
#         freq_i = count_list[i]
#         if freq_i >= mode:
#             mode = freq_i
#             max_idx = i
    
#     print(f'#{tc} {max_idx} {mode}')
    

#### 두번째

import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_12386_숫자카드/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()
    
    cnt_list = [0] * 10
    
    for num in cards:
        cnt_list[int(num)] += 1
    
    mode_num = 0
    mode_cnt = 0
    
    for i in range(10):
        if cnt_list[i] >= mode_cnt:
            mode_cnt = cnt_list[i]
            mode_num = i
    
    print(f'#{tc} {mode_num} {mode_cnt}')