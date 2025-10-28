"""Ramen Bowl"""
def main():
    """main"""
    ans = 1
    check = sorted([int(input()) for _ in range(int(input()))])
    for i in check:
        if check.count(i) > ans:
            ans = check.count(i)
    print(ans)
main()
