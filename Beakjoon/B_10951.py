import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

while True:
    try:
        a, b = map(int, input().split())
    except ValueError:
        break
    except EOFError:
        break
    print(a+b)