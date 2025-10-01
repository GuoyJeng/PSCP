"""SumOfNumber"""
def main():
    """Main"""
    x = int(input())
    plus = 0
    while True:
        num = int(input())
        if num == -1:
            break
        plus += num
        if plus == x:
            break
        if num == x:
            break
    print(plus)
main()
