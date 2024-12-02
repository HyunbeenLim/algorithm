import sys
sys.stdin = open('C:/Users/LHBRR/Desktop/파이썬/알고리즘_스터디/SSAFY_Algorithm/SWEA/SWEA_04408_자기방돌아가기/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # 인덱스가 겹치기만 해도 기다려야 한다
    corrider = [0] * 200
    
    for _ in range(N):
        room1, room2 = map(int, input().split())
        
        # 나오는 방의 수가 더 작게 고정
        if room1 > room2:
            room1, room2 = room2, room1
        
        # 1을 빼줘야 복도 인덱스에 맞출 수 있다
        start = (room1 - 1) // 2
        end = (room2 - 1) // 2
        
        # 학생 별 지나가는 복도 인덱스
        for i in range(start, end + 1):
            corrider[i] += 1
            
    # 복도 리스트의 최댓값 = 겹친 학생 수
    cnt = max(corrider)
    
    print(f'#{tc} {cnt}')