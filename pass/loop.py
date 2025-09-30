"""hee yai yai"""
def main():
    a,b = map(int,input().split())
    num = 0
    cal = a * b
    for i in range(a):
        l = []
        for j in range(b):
            num += 1
            if i > 0 and j > 0:
                l.append(cal)
                continue
            l.append(f'{num:2d}')
        print(*l)
main()
