# 대칭 길이 찾는 함수
def sym_len(idx):
    global max_sym
    cnt = 1
    
    # 대칭 길이 찾기
    for i in range(1, N):
        if (0 <= idx - i) and (idx + i < N) and arr[idx - i] == arr[idx + i]:
            cnt += 2
        else:
            break
    # 지금까지 최댓값과 비교
    if max_sym < cnt:
        max_sym = cnt
    # 반환
    return max_sym


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    max_sym = 0
    for i in range(N):
        # 업데이트
        max_sym = sym_len(i)

    print(f'#{tc} {max_sym}')