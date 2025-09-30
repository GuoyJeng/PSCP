"""Easy Histogram"""
def main():
    """main"""
    x = input().replace(" ","")
    ans = {}
    for i in x:
        num = 0
        for j in x:
            if i == j:
                num += 1
        ans[i] = num
    for i in sorted(ans, key=lambda n: (n.lower(), n.isupper())):
        print(f"{i} = {ans[i]}")
main()
