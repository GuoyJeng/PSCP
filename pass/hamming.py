"""Hamming"""
def main():
    """main"""
    x = input()
    y = input()
    print(list(a != b for a,b in zip(x,y)))
main()
