"""Pig"""
def main():
    """main"""
    x = int(input())
    check = list(map(int, input().split()))
    ans = []
    for i in range(x):
        ans.append(max(check[0 + 2 * i], check[1 + 2 * i]))
    print(" + ".join(map(str, ans)) + " = " + str(sum(ans)) if len(ans) > 1 else str(ans[0]))
main()
