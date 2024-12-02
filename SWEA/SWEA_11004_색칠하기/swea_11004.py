import sys
sys.stdin = open("C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_11004_색칠하기/sample_input.txt", "r")

T = int(input())

def violet_count(r1, c1, r2, c2, color):
    global matrix
    
    cnt = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if matrix[r][c] == 0:
                matrix[r][c] = color
            else:
                if matrix[r][c] != 3 and matrix[r][c] != color:
                    matrix[r][c] += color
                    # 더한 뒤 3이면 cnt 올려주기
                    if matrix[r][c] == 3:
                        cnt += 1
    return cnt
    

for tc in range(1, T + 1):
    # 칠하는 횟수
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]
    
    violet = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        violet += violet_count(r1, c1, r2, c2, color)
    
    print(f'#{tc} {violet}')