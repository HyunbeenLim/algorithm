# 첫 min/max값만 찾고 1빼고 더하기 한 다음에 다음에 바로 그 친구 이상인 친구 발견하면 거기서 연산
# input = sys.stdin.readline

#### 첫번째

# for i in range(1, 11):
#     max_dump = int(input())
#     box_heights = list(map(int, input().split()))
#     box_len = len(box_heights)

#     curr_max = box_heights[0]
#     curr_min = box_heights[0]
#     max_idx = 0
#     min_idx = 0

#     dump = 0
#     while True:
#         dump += 1
        
#         for j in range(box_len):
#             if curr_max <= box_heights[j]:
#                 curr_max = box_heights[j]
#                 max_idx = j
#             elif curr_min >= box_heights[j]:
#                 curr_min = box_heights[j]
#                 min_idx = j
        
#         box_heights[max_idx] -= 1
#         box_heights[min_idx] += 1
#         curr_max -= 1
#         curr_min += 1

#         diff = curr_max - curr_min

#         # 최대 덤핑에 도달하거나 최대 최소의 차이가 1 이하면 break
#         if (dump == max_dump) or (diff <= 1):
#             break

#     for j in range(box_len):
#         if curr_max <= box_heights[j]:
#             curr_max = box_heights[j]
#         elif curr_min >= box_heights[j]:
#             curr_min = box_heights[j]
    
#     diff = curr_max - curr_min

#     print(f'#{i} {diff}')


#### 두번째

import sys
sys.stdin = open("C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_01208_flatten/input.txt", "r")

N = 100
for tc in range(1, 11):
    max_dump = int(input())
    boxes = list(map(int, input().split()))
    
    temp = 0
    curr_max = boxes[0]
    curr_min = boxes[0]
    max_idx = 0
    min_idx = 0
    
    while True:
        temp += 1
        
        # 현재 최대, 최소 높이
        for i in range(N):
            if curr_max <= boxes[i]:
                curr_max = boxes[i]
                max_idx = i
            elif curr_min >= boxes[i]:
                curr_min = boxes[i]
                min_idx = i
        
        # 덤핑
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        curr_max -= 1
        curr_min += 1
        
        if temp == max_dump:
            break
        
    # 덤핑 후 최대 최소
    for i in range(N):
        if curr_max <= boxes[i]:
             curr_max = boxes[i]
        elif curr_min >= boxes[i]:
            curr_min = boxes[i]
    diff = curr_max - curr_min

    print(f'#{tc} {diff}')