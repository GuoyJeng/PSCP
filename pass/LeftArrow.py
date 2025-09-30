"""Left Arrow"""
def main():
    """main"""
    x = int(input())
    n = int(input())
    middle = int(n / 2)
    for i in range(n):
        if i < middle:
            print(" " * (middle - i) + "*" * x)
            continue
        if i > middle:
            print(" " * (i - middle) + "*" * x)
            continue
        print("*" * x)
main()
