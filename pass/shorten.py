"""Shorten"""
def main():
    """main"""
    count = 0
    result = ''
    check = ''
    while True:
        num = int(input())
        if num == -1:
            if check:
                result += str(count)
            break
        if abs(num - count) == 1:
            count = num
            if check == '-':
                continue
            if num == 1 and count == 1 and result != "0":
                result += '1'
                continue
            result += '-'
            check += '-'
            continue
        if count and check == '-':
            result += str(count) + ', '
        elif count:
            result += ', '
        count = num
        result += str(count)
        check = ''
    print(result)
main()
