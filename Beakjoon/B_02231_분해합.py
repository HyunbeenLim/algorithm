import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

# 시작 수
current_number = max(1, N - 9 * (len(str(N))))

# 각 자리수의 합을 구하는 함수
def cal_sum(number):
    sum_value = 0
    while number > 0:
        sum_value += number % 10
        number //= 10
    return sum_value

while current_number < N:
    # 분해합
    sep_sum = current_number + cal_sum(current_number)
    if sep_sum == N:
        break
    current_number += 1

if current_number < N:
    print(current_number)
else:
    print(0)