"""Stair"""
def main():
    """main"""
    y = float(input())
    n = int(input())
    count_step = 0
    long = 0
    sumlong = 0
    for _ in range(n):
        x = float(input())
        long += x
        sumlong += x
        if long >= x:
            long -= y
            count_step += 1
    if long > 0:
        count_step += 1
    if long > 0 and y * n < sumlong:
        print('No')
    else:
        print(count_step)
main()
