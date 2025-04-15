def solution(n, lost, reserve):
    actual_lost = list(set(lost) - set(reserve))
    actual_reserve = list(set(reserve) - set(lost))

    for r in sorted(actual_reserve):
        if r - 1 in actual_lost:
            actual_lost.remove(r - 1)
        elif r + 1 in actual_lost:
            actual_lost.remove(r + 1)

    return n - len(actual_lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

###################################################
# n = 학생 수
# lost = 체육복 잃어버린 학생들 번호
# reserve = 여벌 가져온 학생들 번호
# 주의할 점은 여벌을 가져왔지만 체육복 하나를 도난 당한 경우도 있어서, lost와 reserve에 동일한 번호가 존재할 수 있다
# set을 쓰면 교집합 제거에 용이하고, visited도 만들 필요가 없다..!