def is_one(idx):
    while idx >= 5:
        if (idx - 2) % 5 == 0:
            return False
        idx //= 5
    return idx != 2

def solution(n, l, r):
    answer = 0

    for idx in range(l-1, r):
        if is_one(idx):
            answer += 1

    return answer

'''
n = 2일 때 0인 인덱스를 5진수로 나타내고,
n = 3일 때 0인 인덱스를 5진수로 나타내면
인덱스가 5진수로 나타냈을 때 2를 포함하는 경우 반드시 0이라는 걸 알게 됨
그거 기반으로 풀면 된다
'''