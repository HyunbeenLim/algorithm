# dp 라고 하네요~
def solution(stickers):
    n = len(stickers)
    
    # 예외 처리: 스티커가 1개뿐이면 그냥 그것이 최대값
    if n == 1:
        return stickers[0]
    if n == 2:
        return max(stickers[0], stickers[1])
    
    # Case 1: 첫 번째 스티커 포함, 마지막 스티커 제외
    dp1 = [0] * (n - 1)
    dp1[0] = stickers[0]
    dp1[1] = max(stickers[0], stickers[1])
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + stickers[i])
    
    # Case 2: 첫 번째 스티커 제외, 마지막 스티커 포함 가능
    dp2 = [0] * (n - 1)
    dp2[0] = stickers[1]
    dp2[1] = max(stickers[1], stickers[2])
    for i in range(2, n - 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + stickers[i + 1])

    return max(dp1[-1], dp2[-1])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))