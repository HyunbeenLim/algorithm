T = int(input())
factors = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    N = int(input())
    # 지수 리스트
    cnt_list = [0] * 5
    
    for i in range(5):
        factor = factors[i]
        # 지수
        cnt = 0
        # 각 i번째 소인수마다 나머지가 0이 나오지 않을 때까지 나누어줌
        # 나머지가 0이라면 N을 몫으로 업데이트
        while N % factor == 0:
            cnt += 1
            N = N // factor
        # 지수 업데이트
        cnt_list[i] = cnt
    
    print(f'#{tc}', *cnt_list)
    
'''
N = 2^a x ... x 11^e 라는 건
소인수 하나로 나눴을 때 나머지가 0이라는 뜻!
이걸 이용한다
'''