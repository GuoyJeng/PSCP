"""N"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(x):
            if not j or j == x - 1 or (x > i > 0 and j == i):
                print("*",end='')
                continue
            print(" ",end='')
        print()
main()
