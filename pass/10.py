"""X"""
def main():
    """Main"""
    x = int(input())
    cout = 0
    for i in range(x):
        if i == x - 1:
            cout += i + x
    for i in range(1, cout + 1):
        for j in range(1, cout + 1):
            if i == x and j == x:
                print(f'{j:02d}',end=' ')
                continue
            print(f'{i - (i - 1):02d}',end=' ')
        print()
main()
