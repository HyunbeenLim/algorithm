T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    # 양 옆 두 건물 차이 리스트
    empty_floor = [0] * 4
    # 조망권 확보 세대
    view = 0

    for i in range(2, (n - 2)):
        household_i = buildings[i]
        empty_floor = [household_i - buildings[i - 2], household_i - buildings[i - 1],
                       household_i- buildings[i + 1], household_i - buildings[i + 2]]
        # 모두 0 이상일 때, 최소 값을 더해주기
        if all(empty > 0 for empty in empty_floor):
            view += min(empty_floor)

    print(f'#{tc} {view}')


# 밑 코드처럼 해야 오류 안 생김!

for j in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    empty_floor = [0] * 4
    view = 0

    for i in range(2, (n - 2)):
        household_i = buildings[i]
        empty_floor = [household_i - buildings[i - 2], household_i - buildings[i - 1],
                       household_i - buildings[i + 1], household_i - buildings[i + 2]]

        if all(empty > 0 for empty in empty_floor):
            view += min(empty_floor)

    print(f'#{j + 1} {view}')