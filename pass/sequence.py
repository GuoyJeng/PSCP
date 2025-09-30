"""Leap Year"""
def main():
    """Main"""
    x = int(input())
    num = 1
    for i in range(x):
        l = []
        num = 1
        num += x * i
        for j in range(x):
            if not j:
                l.append(num)
                continue
            num += 1
            l.append(num)
        print(*l)
main()
