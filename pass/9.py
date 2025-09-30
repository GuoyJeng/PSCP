"""IX"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(1, x + 1):
            if j < x - i:
                print("  ",end=' ')
                continue
            print(f'{(j - (x - 1 - i)):02d}',end=' ')
        for k in range(i):
            print(f'{i - k:02d}',end=' ')
        print()
main()
