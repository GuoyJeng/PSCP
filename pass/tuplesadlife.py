"""Tuple Sad Life"""
def main():
    """main"""
    x = tuple(input().split())
    y = input()
    collect = x.index(y)
    for _ in range(x.count(y)):
        print(*[collect for _ in range(x.count(y))])
main()
