"""xi"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(1, x + 1):
            if j < x - i:
                print("  ",end=" ")
                continue
            print(f'{(j - (x - 1 - i)):02d}',end='' if j == x and not i else " ")
        for k in range(i):
            print(f'{i - k:02d}',end='' if k == i - 1 else " ")
        print()
    for i in range(x - 1):
        for j in range(1, x + 1):
            if j <= x - x + i + 1:
                print("  ",end=' ')
                continue
            print(f'{j - 1 - i:02d}',end='' if j == x and i == x - 1 else " ")
        for k in range(x - 1,0,-1):
            if k == 1 + i:
                break
            print(f'{k - 1 - i:02d}',end='' if k == 2 + i else " ")
        print()
main()
