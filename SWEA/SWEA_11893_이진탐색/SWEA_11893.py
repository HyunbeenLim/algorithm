import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_11893_이진탐색/sample_input.txt', 'r')

# start = 0, end = N - 1, target = target_list의 elements
def binary_search(start, end, target, direction):
    if start > end:
        return False
    
    mid = (start + end) // 2
    mid_num = search_list[mid]

    if mid_num == target:
        return True

    # 양쪽 구간을 번갈아 선택하면 그대로 진행
    if direction != 'left' and target < mid_num:
        return binary_search(start, mid - 1, target, 'left')
    elif direction != 'right' and target > mid_num:
        return binary_search(mid + 1, end, target, 'right')
    # 아니면 멈추기
    else:
        return False

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    search_list = sorted(list(map(int, input().split())))
    target_list = list(map(int, input().split()))

    cnt = 0
    for target in target_list:
        direction = 'start'
        if binary_search(0, N-1, target, direction):
            cnt += 1
    
    print(f'#{tc} {cnt}')