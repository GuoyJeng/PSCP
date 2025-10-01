"""US Interstate Number System"""
def main():
    """main"""
    x = input()
    if len(x) <= 2:
        check = True
        if not int(x):
            check = False

        if x[-1] == "0" and check:
            print("Horizontal Major Interstate")
            print(f"I-{int(x)}")
        elif x[-1] == "5" and check:
            print("Vertical Major Interstate")
            print(f"I-{int(x)}")
        else:
            print("Others")
    elif len(x) == 3:
        check = False

        if x[-1] == "0" and int(x[1::]):
            check = True
        elif x[-1] == "5" and int(x[1::]):
            check = True

        if not check:
            print("Others")
        else:
            if not int(x[0]) % 2:
                print("Even Minor Interstate")
            else:
                print("Odd Minor Interstate")
            print(f"I-{int(x[1::])}")
main()
