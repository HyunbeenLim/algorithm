###### 기본 아이디어 ######
t = 'TTTTATTATA'
p = 'TTA'

N = len(t)
M = len(p)

cnt = 0

for i in range(N - M + 1):
    for j in range(M):
        if t[i + j] != p[j]:
            break
    else:
        cnt += 1
print(cnt)

###### 함수 ######
def f(t, p):    # 패턴 p와 일치하는 구간의 시작 인덱스 리턴, 일치하는 경우가 없으면 -1 리턴
    N = len(t)
    M = len(p)

    for i in range(N - M + 1):  # 비교 시작 위치
        for j in range(M):
            if t[i + j] != p[j]:
                break   # for j, 다음 글자부터 비교 시작
        else:   # for j가 중단 없이 반복되면
            return i # 패턴을 찾은 것!
    return -1

###### 깃랩 코드 - 패턴 매칭 ######
# 염기서열 (ACTG 네개의 물질)
p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTCATTCCCTGCGCCGCTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)

# 교재에 포함된 패턴 매칭, 비교시 텍스트 인덱스 i가 증가함
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(i - m, t[i - m: i])
        j = 0

# ==================================================
# 비교하는 동안 텍스트 인덱스 i는 시작 위치로 고정
i = 0
while i <= n - m:
    for j in range(m):
        if p[j] != t[i + j]:
            break
    else:
        print(i, t[i:i + m])
        i += m - 1
    i += 1




###### 교수님 코드 - 패턴 매칭 ######

p = 'XYPV'
t = 'EOGGXYPVSY'

n = len(t)
m = len(p)
s = 0
while s <= n - m:
    for s in range(0, n - m + 1):
        found = True
        for i in range(m):
            # p[i] t[s + i]
            if p[i] != t[s + i]:
                found = False
                break
        if found:
            print(t[s:])
            s += m - 1
    s += 1



###### 교재 코드 - 패턴 매칭 ######
p = 'is'
t = 'This is a book~!'
M = len(p)
N - len(t)

def BruteForce(p, t):
    i = 0 # t 인덱스
    j = 0 # p 인덱스

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M    # 검색 성공
    else:
        return -1       # 검색 실패