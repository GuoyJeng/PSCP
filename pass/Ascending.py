"""Ascending Sort"""
def main():
    """main"""
    x = int(input())
    l = []
    for _ in range(x):
        num = int(input())
        l.append(num)
    l.sort()
    for i in l:
        print(i)
main()
