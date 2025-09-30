"""Largest Number"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    z = int(input())
    a = int(str(x) + str(y) + str(z))
    b = int(str(y) + str(z) + str(x))
    c = int(str(z) + str(x) + str(y))
    d = int(str(x) + str(z) + str(y))
    e = int(str(z) + str(y) + str(x))
    f = int(str(y) + str(x) + str(z))
    result = a
    if result < b:
        result = b
    if result < c:
        result = c
    if result < d:
        result = d
    if result < e:
        result = e
    if result < f:
        result = f
    print(result)
main()
