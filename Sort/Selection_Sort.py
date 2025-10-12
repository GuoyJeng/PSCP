"""Selection_Sort"""
def main():
    """main"""
    num = []
    while True:
        x = input()
        if x == "END":
            break
        num.append(int(x))
    for i,_ in enumerate(num):
        check = min(num[i:])
        lo = num.index(check)
        num[i], num[lo] = num[lo], num[i]
    for i in num:
        print(i)
main()
