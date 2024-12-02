T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    daily_price = list(map(int, input().split()))
    profit = 0

    while True:
        if bool(daily_price) is False:
            break
        sell_day = daily_price.index(max(daily_price))
        max_price = max(daily_price)

        sell_list = daily_price[:sell_day]
        rest = daily_price[sell_day + 1:len(daily_price)]

        for i in range(len(sell_list)):
            daily_profit = max_price - sell_list[i]
            profit += daily_profit

        daily_price = rest

    print(f'#{test_case} {profit}')