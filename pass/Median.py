"""Median"""
def main():
    """main"""
    x = list(map(float,input().split(',')))
    x.sort()
    if not len(x) % 2:
        med = (len(x) / 2) - 1
        med1 = med + 1
        cal = (x[int(med)] + x[int(med1)]) / 2
        print(f'{cal:.2f}')
    else:
        med = round(len(x) / 2)
        print(f'{x[med]:.2f}')
main()
