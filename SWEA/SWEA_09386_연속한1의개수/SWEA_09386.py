T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    seq = input()
    
    # 최댓값
    max_cnt = float('-inf')
    
    while True:
        cnt = 0
        # 1이면 cnt 늘려주기
        for i in range(len(seq)):
            if int(seq[i]):
                cnt += 1
            # 0이면 seq 업데이트 후 다음 반복으로
            else:
                seq = seq[(i + 1):]
                break
        if max_cnt < cnt:
            max_cnt = cnt
        
        # 남은 str이 모두 1이면 while 탈출
        if '0' not in seq:
            break
    # 남은 1의 개수 세서 max 업데이트
    if seq:
        cnt = len(seq)
    if max_cnt < cnt:
        max_cnt = cnt
                
    print(f'#{tc} {max_cnt}')