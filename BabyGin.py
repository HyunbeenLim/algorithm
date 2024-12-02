# 입력 값이 123456처럼 붙여서 입력될 때 리스트로 만들어줌
card = list(map(int, input()))

count = [0] * 12
for number in card:
    count[number] += 1

tri = run = 0

number = 0

while True :
    if count[number] >= 3:
        count[number] -= 3
        tri += 1
        continue
    if count[number] >= 1 and count[number + 1] >= 1 and count[number + 2] >= 1:
        count[number] -= 1
        count[number + 1] -= 1
        count[number + 2] -= 1
        run += 1
        continue

    number += 1
    if number == 10:
        break

if run + tri == 2:
    print('BabyGin')
else:
    print('Lose')
