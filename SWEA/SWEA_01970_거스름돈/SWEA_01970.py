currency = {'a':50000, 'b':10000, 'c':5000, 'd':1000, 'e':500, 'f':100, 'g':50, 'h':10}

T = int(input())

for tc in range(1, T + 1):
    change = int(input())
    numbers = []        # 돈의 개수 리스트
    
    # 가장 가치가 큰 화폐부터 거스름돈과 비교
    # 해당 반복의 화폐가 거스름돈보다 크면 0을 append
    # 작으면 몫을 append, 거스름돈을 나머지로 업데이트
    for value in currency.values():
        if value > change:
            numbers.append(0)
        elif value <= change:
            numbers.append(change // value)
            change = (change % value)
        elif change == 0:
            break
    
    print(f'#{tc}')
    print(*numbers)
    
    