"""HorizontalHistogram"""
def main():
    """main"""
    x = input()
    check = {}
    big = {}
    for i in x:
        if i.isupper():
            big[i] = x.count(i)
            continue
        check[i] = x.count(i)

    for i in sorted(check):
        change = ""
        collect = ""
        for j in range(1,check[i] + 1):
            collect += "-"
            change += "-"
            if not j % 5:
                if not check[i] % 5 and j == check[i]:
                    break
                collect += "|"
                change = ""
        check[i] = collect

    for i in sorted(big):
        change = ""
        collect = ""
        for j in range(1,big[i] + 1):
            collect += "-"
            change += "-"
            if not j % 5:
                if not big[i] % 5 and j == big[i]:
                    break
                collect += "|"
                change = ""
        big[i] = collect

    for i in sorted(check):
        print(f"{i} : {check[i]}")

    for i in sorted(big):
        print(f"{i} : {big[i]}")
main()
