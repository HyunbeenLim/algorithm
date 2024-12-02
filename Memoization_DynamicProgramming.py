def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


## memoization
def fibo1(n):
    if n >= 2 and memo[n] == 0:
            memo[n] = fibo1(n - 1) + fibo1(n - 2)
    return memo[n]


## dynamic programing
def fibo2(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(1, n + 1):
        f[i] = f[i - 1] +f[i - 2]
    
    return f[n]

n = 7

memo = [0] * (n + 1)
memo [0] = 0
memo[1] = 1
print(fibo(n))
print(fibo1(n))




############# 교수님

def comb(n, r):
    if r == 0 or n == r:
        return 1
    else: 
        return comb(n - 1, r - 1) + comb(n - 1, r)
    
memo = [[0] * 50 for _ in range(50)]
def comb1(n, r):
    if r == 0 or n == r:
        return 1
    if memo[n][r]:
        return memo[n][r]
    memo[n][r] = comb1(n - 1, r - 1) + comb1(n - 1, r)
    return memo[n][r]

def comb2(n, r):
    memo = [[0] * 50 for _ in range(50)]
    for i in range(n + 1):
        for j in range(i + 1):
            if j == 0 or i == j:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
    return memo[n][r]