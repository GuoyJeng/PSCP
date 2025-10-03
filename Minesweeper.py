"""Minesweeper"""
def main():
    """main"""
    x = input().split()
    l = []
    for _ in range(int(x[-1])):
        l.append(input().split())
    for a,b in enumerate(l):
        for j in range(len(b)):
            n = 8
            if (not a and not j) or (a == len(l) - 1 and j == len(b) - 1):
                n = 3
            if not a or a == len(l) - 1 or not j or j == len(b) - 1:
                n = 5
        for j in range(n):
main()
