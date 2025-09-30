"""113"""
def main():
    """check"""
    x = input()
    result = ""
    for i in x:
        if "113" in result:
            y = result[:len(result) - 3]
            result = y
        result += i
    if "113" in result:
        y = result[:len(result) - 3]
        result = y
    print(result)
main()
