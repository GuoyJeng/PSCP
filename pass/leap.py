"""Leap Year"""
def main():
    """Main"""
    x = int(input())
    y = int(input())
    num = 0
    for _ in range(x):
        l = []
        for _ in range(1, y + 1):
            num += 1
            if len(l) == y:
                l.append(num)
                break
            l.append(num)
        print(*l)
main()
