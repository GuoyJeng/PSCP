"""Meteorite"""
def main():
    """main"""
    a = float(input())
    b = int(input())
    c = float(input())
    cout = 0
    n = 0
    while a >= c:
        a /= b
        cout += b ** n
        n += 1
    print(cout)
main()
