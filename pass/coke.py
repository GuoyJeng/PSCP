"""Coke"""
def main():
    """heheha"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    num = 0
    num1 = 0
    for i in range(1,d + 1):
        if not b:
            num += a
            continue
        if not i % b:
            if i == d:
                num += a
                break
            num1 += c
        else:
            num += a
    print(num + num1)
main()
