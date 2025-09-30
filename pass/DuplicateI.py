"""Duplicate I"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    check = []
    ans = []
    for _ in range(1, x + y + 1):
        num = int(input())
        if num in check:
            ans.append(num)
        check.append(num)
    if not ans:
        print("Nope")
    else:
        for i in sorted(ans)[::-1]:
            print(i)
main()
