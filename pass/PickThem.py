"""heheha"""
import json
def main():
    """main"""
    x = json.loads(input())
    cout = 0
    for i in x:
        if not i % 2:
            print(i)
            continue
        cout += 1
    if cout == len(x):
        print('Nope')
main()
