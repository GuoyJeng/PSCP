"""Century"""
import math as m
def main():
    """main"""
    x = int(input())
    for _ in range(x):
        a,b = input().split()
        b = int(b)
        if a == "B.E.":
            b -= 543
            if b % 100 > 0:
                print(m.ceil(b / 100))
            else:
                print(m.floor(b / 100))
        elif a == "A.D.":
            if b % 100 > 0:
                print(m.ceil(b / 100))
            else:
                print(m.floor(b / 100))
        else:
            print("ERROR")
main()
