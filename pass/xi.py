"""XI"""
def main():
    x = int(input())
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if j == 1 or i == x:
                print(f'{j:02d}',end=' ')
                continue
            print(f'{i:02d}',end=' ')
        for j in range(x - 1, 0, -1):
            if i == 1 :
                print(f'{i:02d}',end='' if j == 1 else ' ')
                continue
            print(f'{j:02d}',end='' if j == 1 else ' ')
        print()
main()
