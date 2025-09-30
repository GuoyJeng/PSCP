"""bigframe"""
def main():
    """main"""
    a = input().strip()
    b = input().strip()
    c = input().strip()
    d = input().strip()
    e = input().strip()
    laya = max(len(a),len(b),len(c),len(d),len(e))
    print("*" * (laya + 4))
    print("* " + a + (" " * (laya - len(a))) + " *")
    print("* " + b + (" " * (laya - len(b))) + " *")
    print("* " + c + (" " * (laya - len(c))) + " *")
    print("* " + d + (" " * (laya - len(d))) + " *")
    print("* " + e + (" " * (laya - len(e))) + " *")
    print("*" * (laya + 4))
main()
