"""7heheha"""
def main():
    """heheha"""
    num = int(input())
    for i in range(num):
        l = []
        for j in range(1, i + 2):
            l.append(j)
        print(*l)
    for i in range(num - 1, 0, -1):
        l = []
        for j in range(1, i + 1):
            l.append(j)
        print(*l)
main()
