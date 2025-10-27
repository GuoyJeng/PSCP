"""calculate"""
def cal():
    """calculate"""
    num = int(input())
    cout = 0
    for i in range(1,num + 1):
        cout += len(str(i))
    if num == 1:
        print(num)
    else:
        print(cout + num)
cal()
