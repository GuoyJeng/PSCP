"""Giraffe"""
def main():
    """main"""
    n = int(input())
    check = []
    count = 0
    for _ in range(n):
        num = int(input())
        check.append(num)
    if len(check) == 1:
        print(1)
    else:
        for a,b in enumerate(check):
            if a in (0, n - 1) and b > (check[a + 1] if not a else check[a - 1]):
                count += 1
                continue
            if check[a - 1] < b > check[a + 1]:
                count += 1
                continue
        print(count)
main()
