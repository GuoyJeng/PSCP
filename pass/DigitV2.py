"""Digit v2"""
def main():
    """main"""
    x = input()
    if "thousand" in x:
        print(4)
    elif "hundred" in x:
        print(3)
    elif "teen" in x or "ty" in x or "eleven" in x or "twelve" in x or "ten" in x:
        print(2)
    else:
        print(1)
main()
