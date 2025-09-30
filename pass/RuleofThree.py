"""RuleofThree"""
def main():
    """main"""
    item = int(input())
    result = 0
    ans = ""
    get_price = 0
    for _ in range(item):
        price = float(input())
        weight = float(input())
        cal = weight / price
        if result < cal or (result == cal and get_price > price):
            result = cal
            get_price = price
            ans = f"{price:.2f} {weight:.2f}"
    return ans
print(main())
