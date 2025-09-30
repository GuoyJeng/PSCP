"""bubble"""
def main():
    """main"""
    x,y = input().split()
    a,b,c = input().split()

    y = int(y)
    b,c = int(b),int(c)

    l = {"H":5, "O":3, "J":2}
    y *= l[x]

    if a == "R":
        if b == 1:
            c *= 12
        if b == 2:
            c *= 18
        if b == 3:
            c *= 25
    if a == "T":
        if b == 1:
            c *= 15
        if b == 2:
            c *= 20
        if b == 3:
            c *= 30
    if a == "M":
        if b == 1:
            c *= 10
        if b == 2:
            c *= 15
        if b == 3:
            c *= 20
    print(c + y)
main()
