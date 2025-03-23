def check(wallet, bill):
    for i in range(2):
        if wallet[i] < bill[i]:
            return False
    return True

def solution(wallet, bill):
    cnt = 0

    while True:
        if check(wallet, bill):
            return cnt
        else:
            bill[0], bill[1] = bill[1], bill[0]
            if check(wallet, bill):
                return cnt
        
        # 접기
        longer = bill.index(max(bill))
        bill[longer] //= 2
        cnt += 1


print(solution([30, 15], [26, 17]))
print(solution([50, 50], [100, 241]))