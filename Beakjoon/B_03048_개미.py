import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())
group1 = input()
group2 = input()
time = int(input())

ants = []

for i in range(a-1, -1, -1):
    ants.append([group1[i], '>'])

for i in range(b):
    ants.append([group2[i], '<'])

for t in range(time):
    jump = []
    for j in range(a+b-1):
        if ants[j][1] == '>' and ants[j+1][1] == '<':
            jump.append(j)
    for ant in jump:
        ants[ant], ants[ant+1] = ants[ant+1], ants[ant]

ans = ''

for ant in ants:
    ans += ant[0]

print(ans)