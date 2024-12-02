import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12391/sample_input.txt", "r")
# input = sys.stdin.readline

# 이진 탐색
def Binary_search(lst, key):
    n = len(lst)

    start_idx = 0
    end_idx = n - 1
    
    cnt = 0
    while start_idx <= end_idx:
        cnt += 1
        middle_idx = int((start_idx + end_idx) / 2)
        if lst[middle_idx] == key:
            return cnt
        elif lst[middle_idx] > key:
            end_idx = middle_idx
        else:
            start_idx = middle_idx
    return 0

T = int(input())

for tc in range(1, T + 1):
    p, a, b = map(int, input().split())

    # 페이지 리스트
    p_list = list(range(1, p + 1))

    # a, b 시도 횟수 // 0이 나오는 경우는 없음
    a_count = Binary_search(p_list, a)
    b_count = Binary_search(p_list, b)

    if a_count < b_count:
        ans = 'A'
    elif a_count > b_count:
        ans = 'B'
    else:
        ans = 0
    
    print(f'#{tc} {ans}')