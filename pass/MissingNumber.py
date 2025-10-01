"""MissingNumber"""
def main():
    """main"""
    num = int(input())
    check = set(i for i in range(1, num + 1))
    ans = set()
    while True:
        x = int(input())
        if not x:
            break
        ans.add(x)
    for i in sorted(check.difference(ans)):
        print(i)
main()
