"""Point Sorting"""
def main():
    """main"""
    x = int(input())
    for _ in range(x):
        y = int(input())
        check = []
        for _ in range(y):
            z = list(map(int, input().split()))
            check.append(z)
        for _,_ in enumerate(check):
            for j in range(len(check) - 1):
                if sum(check[j]) > sum(check[j + 1]):
                    check[j], check[j + 1] = check[j + 1], check[j]
                    continue
                if sum(check[j]) == sum(check[j + 1]):
                    if check[j][1] < check[j + 1][1]:
                        check[j], check[j + 1] = check[j + 1], check[j]
        print(j for j in check)
main()
