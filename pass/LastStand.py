"""LastStand"""
def main():
    """main"""
    x = input().strip("[]")
    l = x.split(",")
    for i in l:
        print(i[-1])
main()
