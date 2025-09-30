"""VerticalHistogram"""
def main():
    """main"""
    x = input()
    check = {}
    for i in x:
        if i.isalpha():
            check[i] = x.count(i)
    for i in range(max(check.values()), -1, -1):
        l = ""
        if not i:
            print(" " * 3,end=" ")
        else:
            print(f"{i:2d}",end="  ")
        for _,b in enumerate(sorted(check)):
            if not i:
                print(*sorted(check),end="")
                break
            if check[b] >= i:
                l += "* "
                continue
            l += "  "
        print(l.rstrip())
main()
