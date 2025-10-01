"""Matrix"""
def main():
    """main"""
    m = int(input())
    n = int(input())
    for _ in range(m):
        l = []
        for _ in range(n):
            num = int(input())
            l.append(num)
        print(*l)
main()
