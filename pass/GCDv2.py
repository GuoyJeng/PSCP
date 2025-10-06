"""GCD V.2"""
def main(num1, num2):
    """main"""
    if not num2:
        return num1
    return main(num2, num1 % num2)
print(int(main(float(input()), float(input()))))
