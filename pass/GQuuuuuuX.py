"""GQuuuuuuX"""
def main():
    """main"""
    check_u = ''
    count_u = 0
    check = ''
    for i in input().lower():
        if i == 'g' and not check:
            check += 'g'
            continue
        if i == 'q' and check == 'g':
            check += 'q'
            continue
        if i == 'u' and check == 'gq':
            check_u += 'u'
            continue
        if i == 'x' and len(check_u) > 0 and check == 'gq':
            if len(check_u) > count_u:
                count_u = len(check_u)
            check_u = ''
            check = ''
            continue
        check = ''
    print('None' if not count_u else count_u)
main()
