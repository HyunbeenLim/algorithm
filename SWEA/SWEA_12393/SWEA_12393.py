import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12393/sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    str_1 = input()
    str_2 = input()

    str_len = len(str_1)

    start_idx = 0
    end_idx = str_len

    cnt = 0
    while True:
        if str_1 == str_2[start_idx:end_idx]:
            cnt += 1
            start_idx += 1
            end_idx += 1
        else:
            start_idx += 1
            end_idx += 1
        
        if end_idx > len(str_2):
            break
    
    print(f'#{tc} {cnt}')


