"""Sort"""
def main():
    """main"""
    num = []
    while True:
        x = input()
        if x == "END":
            break
        num.append(int(x))
    for a,_ in enumerate(num):
        for i,_ in enumerate(num):
            if num[a] < num[i]:
                num[a], num[i] = num[i], num[a]
    for i in num:
        print(i)
main()
