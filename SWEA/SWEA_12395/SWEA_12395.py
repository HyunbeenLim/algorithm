import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12395/sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    str_1 = input()
    str_2 = input()

    cnt_list = [0] * len(str_1)

    for char in str_2:
        for i in range(len(str_1)):
            if str_1[i] == char:
                cnt_list[i] += 1
    
    max_cnt = 0
    for cnt in cnt_list:
        if cnt >= max_cnt:
            max_cnt = cnt
    
    print(f'#{tc} {max_cnt}')