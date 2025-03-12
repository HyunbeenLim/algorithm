import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
dna = input()

# A C G T
acgt = list(map(int, input().split()))
must_have = {
    'A': acgt[0],
    'C': acgt[1],
    'G': acgt[2],
    'T': acgt[3]
}

false_cnt = 0
for key, value in must_have.items():
    if value != 0:
        false_cnt += 1

# 시작 문자열
start = 0
end = K-1
start_string = dna[start:end+1]

for s in start_string:
    if must_have[s] == 1:
        false_cnt -= 1
    must_have[s] -= 1
        
ans = 0

if false_cnt == 0:
    ans += 1

# start + 1 해주면 이전 start 위치의 알파벳 값 + 1 -> 더하기 이전 값이 0일 때만 false_cnt 올려주기
# end + 1 해주면 1을 더한 이후 end 위치의 알파벳 값 -1 -> 빼기 이전 값이 1일 때 false_cnt 내려주기

while end < N-1:
    if must_have[dna[start]] == 0:
        false_cnt += 1
    must_have[dna[start]] += 1
    
    start += 1
    end += 1

    if must_have[dna[end]] == 1:
        false_cnt -= 1
    must_have[dna[end]] -= 1

    if false_cnt == 0 and dna[start:end+1]:
        ans += 1

print(ans)