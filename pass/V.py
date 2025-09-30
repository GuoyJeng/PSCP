"""van"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        l = []
        for j in range(1,i+2):
            l.append(j)
        print(*l)
main()
