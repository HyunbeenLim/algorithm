import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

# 지금 시간 초과(지금 많이 걸리긴 함)
#### start, end 늘려가면서 등장 숫자에 +- 1씩 해줘야 할 듯 -> 생각해보기

N, K = map(int, input().split())
dna = input()

# A C G T
must_have = list(map(int, input().split()))

start = 0
end = K

used = set()
ans = 0

# 제약조건 만족하는지 확인
def check_validity(string):
    copy_list = []

    for cnt in must_have:
        copy_list.append(cnt)
    
    for s in string:
        if s == 'A' and copy_list[0] != 0:
            copy_list[0] -= 1
        elif s == 'C' and copy_list[1] != 0:
            copy_list[1] -= 1
        elif s == 'G' and copy_list[2] != 0:
            copy_list[2] -= 1
        elif s == 'T' and copy_list[3] != 0:
            copy_list[3] -= 1
    
    return sum(copy_list) == 0

while end <= N:
    temp_string = dna[start:end]

    if temp_string not in used:
        if check_validity(temp_string):
            used.add(temp_string)
            ans += 1
    
    start += 1
    end += 1

print(ans)