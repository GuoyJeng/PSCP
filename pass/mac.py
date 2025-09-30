"""Mac"""
def check(x: str):
    """check"""
    count = ''
    block = 0
    if '-' in x and ':' in x:
        return False
    for i in x:
        if i.isnumeric() or i.lower() in ('a','b','c','d','e','f'):
            count += i
        elif i in ('-',':') and len(count) == 2:
            block += 1
            count = ''
        elif i == '.' and len(count) == 4:
            block += 1
            count = ''
        else:
            return False
    if len(count) == 2 and ('-' in x or ':' in x):
        block += 1
    elif len(count) == 4 and ('.' in x):
        block += 1
    else:
        return False
    if block == 6 and ('-' in x or ':' in x):
        return True
    if block == 3 and '.' in x:
        return True
    return False
def main(x):
    """main"""
    if check(x) and '-' in x:
        return "VALID 1"
    if check(x) and ':' in x:
        return "VALID 2"
    if check(x) and '.' in x:
        return "VALID 3"
    return "ERROR"
print(main(input()))
