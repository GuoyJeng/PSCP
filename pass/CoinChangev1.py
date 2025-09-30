"""CoinChangev1"""
def main():
    """main"""
    x = int(input())
    coin = 0
    while x > 0:
        if x >= 25:
            num = x // 25
            coin += num
            x %= 25
        elif x >= 10:
            num = x // 10
            coin += num
            x %= 10
        elif x >= 5:
            num = x // 5
            coin += num
            x %= 5
        elif x >= 1:
            coin += x
            x -= x
    print(coin)
main()
