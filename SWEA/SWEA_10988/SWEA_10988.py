# 선택 정렬
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    
    number_list = list(map(int, input().split()))
    
    # 선택 정렬
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if number_list[j] < number_list[min_idx]:
                min_idx = j
        number_list[i], number_list[min_idx] = number_list[min_idx], number_list[i]

    # unique 값 정리
    unique = []
    for i in range(N):
        if number_list[i] not in unique:
            unique.append(number_list[i])
    
    print(f'#{tc} {unique[K - 1]}')
    
    
    

# count로 해보기
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split()) # N = 정수의 수, K = K번째 작은수
    arr = list(map(int,input().split()))

    M = max(arr)

    count_list = [0] * (M+1)

    # 요소의 갯수 리스트에 담기
    for i in range(N):
        count_list[arr[i]] += 1


    cnt = K
    
    # count_list를 순서대로 돌면서 등장한 숫자라면 cnt(K)를 하나씩 뺌
    # K에서 1이 빼지면서 0이 된 순간 순회를 중단하고 j 반환
    # j는 인덱스 역할이라 + 1이 되어 있어도 알아서 잘 출력됨
    
    for j in range(M+1):
        if count_list[j] != 0:
            cnt -= 1
        if cnt == 0:
            break
    
    print(f'#{test_case} {j}')