import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_3499_퍼펙트셔플/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    str_list = input().split()
    str_to_print = [0] * N
    
    # 중간 인덱스
    center_idx = (N - 1) // 2
    
    # while 종료 조건(출력할 리스트의 인덱스 기능과 같다)
    idx_to_print = 0
    
    # 위에 쌓이는 카드 인덱스
    upper = 0
    
    # 아래에 쌓이는 카드 인덱스
    lower = center_idx + 1
    
    while idx_to_print < N:
        # 중간 인덱스를 포함하는 구간까지 위에 겹침
        if upper <= center_idx:
            str_to_print[idx_to_print] = str_list[upper]
            upper += 1
            idx_to_print += 1
        # 중간 인덱스 + 1부터 N-1까지 아래에 겹침
        if lower < N:
            str_to_print[idx_to_print] = str_list[lower]
            lower += 1
            idx_to_print += 1
    
    print(f'#{tc}', *str_to_print)
            
    