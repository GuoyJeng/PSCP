"""Data Spike"""
def main():
    """main"""
    num = int(input())
    l = []
    for _ in range(num):
        x = input()
        l.append(x)
    l.sort(key=len)
    for i in l:
        print(i)
main()
