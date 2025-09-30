"""Run Length Encoding"""
def main():
    """main"""
    x = input()
    count = 0
    process = ''
    result = ''
    for i in x:
        process += i
        if i != process[0]:
            count = len(process)
            result += str(count - 1) + process[0]
            process = i
    result += str(len(process)) + process[0]
    print(result)
main()
