"""Squid Game 3"""
def main():
    """main"""
    a = 0
    b = 0
    for i in range(20):
        add = int(input())
        if i < 10:
            a += add
        else:
            b += add
    if a > b:
        print("B")
    elif b > a:
        print("A")
    elif a == b:
        print("AB")
main()
