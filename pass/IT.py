"""IT Business"""
def main():
    """"main"""
    x = float(input())
    y = float(input())
    check = 0
    while True:
        if check == 3:
            break
        num = input()
        if num == "end":
            break
        if num[0] == "D":
            if y >= float(num[2:]):
                x += float(num[2:])
                y -= float(num[2:])
            elif y < float(num[2:]):
                check += 1
                continue
        elif num[0] == "W":
            if x >= float(num[2:]):
                x -= float(num[2:])
                y += float(num[2:])
            elif x < float(num[2:]):
                check += 1
                continue
        check = 0
    print(f"{x:.2f}")
    print(f"{y:.2f}")
main()
