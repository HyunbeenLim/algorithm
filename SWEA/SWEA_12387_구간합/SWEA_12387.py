
#### 처음 풀었을 때

# T = int(input())

# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     num_list = list(map(int, input().split()))

#     sum_list = [0] * n
#     sum_list[0] = num_list[0]

#     for i in range(1, n):
#         sum_list[i] = sum_list[i - 1] + num_list[i]

#     min_sum = sum_list[m - 1]
#     max_sum = sum_list[m - 1]

#     for j in range(m, n):
#         section_sum = sum_list[j] - sum_list[j - m]
#         if section_sum < min_sum:
#             min_sum = section_sum
#         elif section_sum > max_sum:
#             max_sum = section_sum

#     print(f'#{tc} {max_sum - min_sum}')





#### 두번째 풀기

import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SwEA/SWEA_12387_구간합/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sum_list = [0] * N
    sum_list[0] = arr[0]
    
    for i in range(1, N):
        sum_list[i] = sum_list[i-1] + arr[i]
    
    # 첫 M개의 합으로 초기값 설정
    min_sum = sum_list[M - 1]
    max_sum = sum_list[M - 1]

    for j in range(M, N):
        m_sum = sum_list[j] - sum_list[j-M]
        
        if m_sum < min_sum:
            min_sum = m_sum
        elif m_sum > max_sum:
            max_sum = m_sum

    max_diff = max_sum - min_sum
    print(f'#{tc} {max_diff}')


