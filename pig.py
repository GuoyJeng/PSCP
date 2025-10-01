"""Pig"""
def main():
    """main"""
    x = int(input())
    check = list(map(int, input().split()))
    ans = []
    for a,b in enumerate(check):
        if not a % 2:
            ans.append(b)
    print(ans)
main()
