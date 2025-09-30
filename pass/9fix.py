"""IX"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        l = []
        for j in range(1, x + 1):
            if j < x - i:
                l.append("  ")
                continue
            l.append(f'{(j - (x - 1 - i)):02d}')
        for k in range(i):
            l.append(f'{i - k:02d}')
        print(*l)
main()
