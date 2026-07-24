def solution(brown, yellow):
    # 가능한 후보군
    candidates = []
    # 중복 제거
    unique_set = set()

    # yellow가 1인 경우도 존재해 최소한 1도 탐색할 수 있게 해야 함
    for i in range(1, yellow+1):
        # 곱해서 yellow를 만들 수 있는 모든 경우의 수를 저장(순서만 바뀐 건 제외)
        if yellow % i == 0:
            if (i not in unique_set) and (yellow // i not in unique_set):
                candidates.append([i, yellow//i])
                unique_set.add(i)
                unique_set.add(yellow//i)

    # 저장된 값들을 가져와, brown과 맞는지 확인 후 정답 return
    for candidate in candidates:
        r, c = candidate
        border = 2 * (r + c + 2)
        if border == brown:
            return [c+2, r+2]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))