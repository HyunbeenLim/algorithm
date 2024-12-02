import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/깃/SSAFY_Algorithm/SWEA/SWEA_03143_문자열타이핑/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    text, pattern = input().split()
    N = len(text)
    M = len(pattern)

    cnt = 0
    i, j = 0,0
    while i < N:
        if text[i] != pattern[j]:
            i -= j
            j = -1

        i += 1
        j += 1
        if j == M:
            cnt += 1
            j = 0

    number_of_type = N - (M * cnt) + cnt

    print(f'#{tc} {number_of_type}')

