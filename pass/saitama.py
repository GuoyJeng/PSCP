"""Saitama"""
import math as m
def main():
    x = int(input())
    y = int(input())
    z = int(input())
    a = int(input())
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())
    a1 = int(input())
    cal = m.ceil(x / x1)
    cal1 = m.ceil(y / y1)
    cal2 = m.ceil(z / a1)
    cal3 = m.ceil(a / z1)
    day = cal
    for _ in range(4):
        if day < cal1:
            day = cal1
        elif day < cal2:
            day = cal2
        elif day < cal3:
            day = cal3
    print(day)
main()
