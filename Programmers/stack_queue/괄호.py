def solution(s):
    stack = []

    for frac in s:
        if frac == '(':
            stack.append(frac)
        elif frac == ')' and stack:
            stack.pop()
        else:
            return False

    return True if not stack else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))