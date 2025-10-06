"""GCD V.1"""
from functools import reduce
def gcd(num1, num2):
    """GCD"""
    if not num2:
        return num1
    return gcd(num2, num1 % num2)

def main():
    """main"""
    n = int(input())
    num = [float(input()) for i in range(n)]
    print(int(reduce(gcd, num)))
main()
