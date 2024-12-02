import sys
sys.stdin = open('./sample_input.txt', 'r')

# 조합 재귀
indices = []
N = 2 # 고르는 숫자 수
def comb(lev, start):
    if lev == N:
        exchange(tuple(indices))   # 최대, 최소 업데이트
        return

    for i in range(start, len(idx_list)):
        indices.append(idx_list[i])
        comb(lev + 1, i + 1)
        indices.pop()

# 재귀 함수에서 인덱스를 받아, 숫자 배열과 비교 후 최댓값, 최솟값 업데이트
def exchange(indices):
    global max_number, min_number, number
    i, j = indices

    # 교환
    number[i], number[j] = number[j], number[i]

    temp_number = ''
    # 비교, 업데이트
    for frac in number:
        temp_number += frac
    
    if int(temp_number) == 0:
        max_number = temp_number
        min_number = temp_number
    else:
        if temp_number[0] != '0':   # 유효한 숫자인 경우만 판단
            if int(max_number) <= int(temp_number):
                max_number = temp_number
            if int(min_number) > int(temp_number):
                min_number = temp_number

    # 되돌리기
    number[i], number[j] = number[j], number[i]
    
T = int(input())

for tc in range(1, T + 1):
    raw_number = input()
    number = list(raw_number)
    length = len(number)
    idx_list = list(range(length))
    
    # 초기 최댓값, 최솟값 지정
    max_number = '0'
    min_number = '9' * length 

    comb(0, 0)

    # 바뀌지 않았을 때도 비교
    if int(raw_number) >= int(max_number):
        max_number = raw_number
    if int(raw_number) < int(min_number):
        min_number = raw_number


    print(f'#{tc} {min_number} {max_number}')