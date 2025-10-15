"""Fibonacci V.2"""
memo = {0:0, 1:1}
def Fibo(x):
    """Fibo"""
    if x in memo:
        return memo[x]
    memo[x] = Fibo(x - 1) + Fibo(x - 2)
    return memo[x]
