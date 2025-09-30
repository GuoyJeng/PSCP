"""3nPlus1"""
def main():
    """main"""
    i = 0
    j = 0
    while i < 1:
        x = int(input())
        times = 0
        k = 0
        k += x
        if not x:
            break
        while j < 1:
            times += 1
            if not k % 2:
                k /= 2
                continue
            if k == 1 or not times:
                print(times)
                break
            k = (k * 3) + 1
main()
