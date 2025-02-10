import sys
input = sys.stdin.readline

# 더하는 함수
def cal_sum(numbers):
    value = 0
    for i in range(4):
        if i == 0:
            value += numbers[i]
        elif i == 1:
            value += 5 * numbers[i]
        elif i == 2:
            value += 10 * numbers[i]
        else:
            value += 50 * numbers[i]

    return value

# 개수 조합
def perm(k):
    global number_set

    if k == 4:
        if sum(seq) == N:
            number_set.add(cal_sum(seq))
        return
    
    for i in range(N+1):
        seq[k] = arr[i]
        perm(k + 1)


N = int(input())
arr = list(range(N + 1))        # 0 ~ N
seq = [0] * 4
number_set = set()

perm(0)

print(len(number_set))