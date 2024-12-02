import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_10989_폭격작전/sample_input.txt', 'r')





#### 현희
T = int(input())
# 배열의 크기, 폭탄의 수
for tc in range(1,T+1) :
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    # 최종 답
    ans = 0
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    
    for _ in range(M) :
        r1,c1,d = map(int,input().split())
        # 시작행, 열, 범위
    
        # 투하 위치도 포함, 폭탄마다 리셋
        sum = arr[r1][c1]
        arr[r1][c1] = 0
    
    
        for i in range(4) :
            for j in range(1,d+1) :
                nr = r1 + (dr[i] * j)
                nc = c1 + (dc[i] * j)
                if 0<= nr < N and 0 <= nc < N :
                    sum += arr[nr][nc]
                    # 값이 중복 더해지는 것 방지
                    arr[nr][nc] = 0 
        
        #ans에 저장
        ans += sum
        
    print(f'#{tc} {ans}')