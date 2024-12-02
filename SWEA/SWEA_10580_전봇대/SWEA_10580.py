import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_10580_전봇대/input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    wires = [list(map(int, input().split())) for _ in range(N)]
    
    # 교차점
    cnt = 0
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            # i번째 전선과 비교해서, j번째 전선의 시작점은 크지만 도착점이 더 작다면 한점에서 교차
            if wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
                cnt += 1
            # 반대로 시작점은 작지만 도착점은 더 큰 경우에도 한점에서 교차
            elif wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
                cnt += 1
    
    print(f'#{tc} {cnt}')