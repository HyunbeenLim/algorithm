import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

cnt_lst = [[] for _ in range(51)]

for _ in range(N):
    string = input().strip()
    if string in cnt_lst[len(string)]:
        continue
    cnt_lst[len(string)].append(string)

for frac in cnt_lst:
    if frac:
        frac.sort()
        for ele in frac:
            print(ele)