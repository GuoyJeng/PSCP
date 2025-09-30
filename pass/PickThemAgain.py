"""PickThemAgain"""
def main():
    """main"""
    x = input().split()
    x.reverse()
    check = []
    for i in x:
        if '.' in i:
            x.remove(i)
            continue
        if not int(i) % 3 or not int(i) % 5:
            check.append(int(i))
    if not check:
        print("Nope")
    else:
        for i in check:
            print(i)
main()
