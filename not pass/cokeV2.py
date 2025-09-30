"""Coke"""
def main():
    """heheha"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        print(d * a)
    elif not d % b:
        num = ((d // b) - 1) * c
        num1 = (d - (d // b) + 1)  * a
        print(num + num1)
    else:
        num = (d // b) * c
        num1 = (d - (d // b)) * a
        print(num + num1)
main()
