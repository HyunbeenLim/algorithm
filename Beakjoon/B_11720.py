import sys
input = sys.stdin.readline

N = int(input())
number_list = list(input())

num_sum = int()
for number in number_list:
    num_sum += int(number)
    
print(num_sum)