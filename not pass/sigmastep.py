"""SigmaStep"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    z = int(input())
    num = 0
    while x <= y:
        num += x
        x += z
    print(num)
main()
