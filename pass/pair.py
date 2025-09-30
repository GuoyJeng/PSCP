"""B - Fully pair?"""
def main():
    """main"""
    x = input()
    check1 = ''
    for i in x:
        check = ''
        for j in x:
            if j == i:
                check += j
        if not len(check) % 2:
            continue
        if (len(check) > 2 and not i in check1) or len(check) < 2:
            check1 += i
    if not check1:
        print('fully paired')
    else:
        print(check1)
main()
