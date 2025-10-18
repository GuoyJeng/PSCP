"""Olympic"""
def main():
    """main"""
    num = int(input())
    ans = [input().split() for _ in range(num)]
    ans.sort(key=lambda x: [-int(x[1]), -int(x[2]), -int(x[3]), x[0]])
    rank = []
    for i in range(num):
        if not i:
            rank.append(1)
            continue
        if ans[i][1:] == ans[i - 1][1:]:
            rank.append(rank[-1])
            continue
        rank.append(i + 1)
    for j,i in enumerate(ans):
        print(rank[j], *i, sum([int(i[1]), int(i[2]), int(i[3])]))
main()
