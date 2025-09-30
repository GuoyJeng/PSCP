"""Donut"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    price = 0
    donut = 0
    free = 0
    while donut + free < d:
        price += a
        donut += 1
        if not donut % b:
            free += c
    print(price,donut + free)
main()
