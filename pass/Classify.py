"""Classify"""
def main():
    """main"""
    check = {}
    while True:
        num = input()
        if num == "END":
            break
        check[num[:4]] = check.get(num[:4], 0) + 1
    ans = []
    for i in sorted(check):
        if i[:2] in ans:
            print("--", int(i[2:]), check[i])
            continue
        ans.append(i[:2])
        print(i[:2], int(i[2:]), check[i])
main()
