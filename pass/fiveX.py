"""fiveX"""
def main():
    """main"""
    x = int(input())
    for _ in range(1):
        for j in range(1, x + 1):
            if not j % 5:
                print("X",end='')
            else:
                print("*",end="")
        print()
main()
