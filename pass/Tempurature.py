"""Tempurature"""
def main():
    """main"""
    x = float(input())
    y = input()
    z = input()
    c = 0

    if y == "C":
        c += x
    elif y == "K":
        c += x - 273.15
    elif y == "F":
        c += (x - 32) / (9 / 5)
    elif y == "R":
        c += x / (9 / 5) - 273.15

    if z == "C":
        print(f'{c:.2f}')
    elif z == "K":
        ans = c + 273.15
        print(f'{ans:.2f}')
    elif z == "F":
        ans = c * (9 / 5) + 32
        print(f'{ans:.2f}')
    elif z == "R":
        ans = (c + 273.15) * (9 / 5)
        print(f'{ans:.2f}')
main()
