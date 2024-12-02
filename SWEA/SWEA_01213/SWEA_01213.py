# import sys
# sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_01213/test_input.txt', 'r')

for j in range(10):
    tc = int(input())

    pattern = input()
    text = input()

    M = len(pattern)
    N = len(text)

    cnt = 0

    for i in range(N - M + 1):
        for j in range(M):
            if pattern[j] != text[i + j]:
                break
        else:
            cnt += 1
    
    print(f'#{tc} {cnt}')

