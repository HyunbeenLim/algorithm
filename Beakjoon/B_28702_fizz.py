import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

input_lst = []

for _ in range(3):
    input_lst.append(input())

number = 0
idx = 0

for i in range(3):
    try:
        number = int(input_lst[i])
        idx = i
    except ValueError:
        continue

next_number = number + (3 - idx)

if next_number % 5 == 0 and next_number % 3 == 0:
    print('FizzBuzz')
elif next_number % 3 == 0 and not next_number % 5 == 0:
    print('Fizz')
elif next_number % 5 == 0 and not next_number % 3 == 0:
    print('Buzz')
else:
    print(next_number)