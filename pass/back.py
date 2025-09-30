"""Back"""
def main():
    """main"""
    l = []
    while True:
        x = input()
        if x == "NULL":
            break
        l.append(x)
    for i in range(len(l) - 1, -1, -1):
        print(l[i])
main()
