import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12385/sample_input.txt", "r")
# input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    st_to_charge = list(map(int, input().split()))
    
    # 현재 치
    current_idx = 0
    # 방문 수
    visit = 0 
    while True:
        # 현재 위치 + k를 지금 버스의 목표 도착치로 설정(최대 이동 가능 위치)
        dest_idx = current_idx + k
        
        # 최대 이동 가능 위치가 n보다 크면 break
        if dest_idx >= n:
            break
            
        # break 조건이 만족되지 않을 때
        ## 목표 인덱스부터 뒤로가면서 충전 가능 정류장 탐색
        for i in range(dest_idx, current_idx, -1):
            # 찾으면 방문 횟수 증가
            ## 버스가 거기에 정차해야 하니 현재 위치를 i로 업데이트
            ### for문 탈출해야 다시 그 위치에서 시작할 수 있음
            if i in st_to_charge:
                visit += 1
                current_idx = i
                break
                
        # 다 탐색해도 없다면 0을 반환하게 for-else
        ## for-else는 for문을 다 실행해도 아무 일이 없을 때 else문을 실행
        ### 목표 인덱스부터 원래 위치까지 순회했는데 아무 일도 없었다면
        ### 충전 가능 정류장이 없다는 뜻이므로 0 반환
        else:
            visit = 0
            break
    
    print(f'#{tc} {visit}')

