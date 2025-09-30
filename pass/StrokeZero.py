"""Stroke Zero"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(i + 1):
            if i > j > 0 and x - 1 > i > 0:
                print(1,end='' if j == i else ' ')
                continue
            print(0,end='' if j == i else ' ')
        print()
main()
