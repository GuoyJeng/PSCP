'''rabbit'''
def main():
    '''doc'''
    x = int(input())
    b = 0
    z = ""
    l = []
    l1 = []
    for i in range(x):
        name,wei = input().split()
        l.append(name)
        l1.append(int(wei))
        if int(wei) > 15:
            b += 1
        if l1[i] == max(l1):
            z = l[i]
    y = max(l1)
    print(b)
    print(z,y)
main()
