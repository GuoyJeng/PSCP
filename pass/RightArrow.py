"""Right Arrow"""
def main():
    """main"""
    x = int(input())
    n = int(input())
    middle = int(n / 2)
    for i in range(n):
        if middle >= i > 0:
            print(" " * i + "*" * x)
            continue
        if i > middle:
            middle -= 1
            print(" " * (middle) + "*" * x)
            continue
        print("*" * x)
main()
