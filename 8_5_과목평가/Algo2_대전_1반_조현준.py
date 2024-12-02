T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))  # 입력 데이터

    diff = [0] * N  # 높이 차를 저장하는 list

    # 높이 차이 계산
    for i in range(1, N):  # i: 1 ~ N
        diff[i] = A[i] - A[i-1]

    tmp_ans_arr = list()  # (경사도, 구간길이) Tuple 데이터를 저장하는 변수
    tmp_len = 1  # 구간길이를 저장하는 임시 변수
    tmp_height = 0  # 지나온 구간의 높이를 저장하는 임시 변수

    # 높이 차이가 0 또는 양수인 구간의 합을 구해 경사도와 길이 정보를 저장한다
    for i in range(1, N):  # 높이차 배열을 순회
        difference = diff[i]
        if difference >= 0:  # 높이차가 양수인 경우, 길이 및 높이차 추가
            tmp_len += 1
            tmp_height += difference
        else:  # difference < 0
            if tmp_len > 1 and tmp_height > 0:  # 구간길이가 2 이상, 높이 차이가 0보다 큰 데이터만 저장
                tmp_ans_arr.append((tmp_height / tmp_len, tmp_len))  # (경사도, 구간길이) tuple 저장
            # 임시 변수 초기화
            tmp_len = 1
            tmp_height = 0

    # 반복문 탈출 후, 잔여 데이터 처리
    if tmp_len > 1 and tmp_height > 0:
        tmp_ans_arr.append((tmp_height / tmp_len, tmp_len))

    # 정답 배열에 적어도 1개 이상의 정답 후보가 존재한다면,
    if tmp_ans_arr:
        ans = tmp_ans_arr[0]  # 첫번째 데이터로 초기화
        for tmp_ans in tmp_ans_arr:  # 정답 후보를 순회
            # 경사도가 더 작거나 같으며, 길이가 길거나 같은 데이터가 있다면 정답 갱신
            if tmp_ans[0] <= ans[0] and tmp_ans[1] >= ans[1]:
                ans = tmp_ans
        print(f'#{tc} {ans[1]}')  # tuple 데이터의 1번 인덱스가 가리키는 정보가 구간 길이
    # 정답 배열에 아무런 데이터도 존재하지 않는다면,
    else:
        print(f'#{tc} 0')  # 0 출력
