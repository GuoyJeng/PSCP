"""One for All"""
def main():
    """main"""
    x = int(input())
    ans = ""
    for i in range(1, x + 1):
        name = input()
        ans += name
        if i == x:
            ans += f'_{i}'
            continue
        if not i % 2:
            ans += "-" * i
            continue
        ans += "*" * i
    print(ans)
main()
