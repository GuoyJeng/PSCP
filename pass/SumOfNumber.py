"""SumOfNumber"""
def main():
    """Main"""
    x = int(input())
    plus = 0
    while True:
        num = int(input())
        if num == -1:
            break
        if num == x:
            plus += num
            break
        plus += num
    print(plus)
main()
