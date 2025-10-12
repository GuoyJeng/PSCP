"""Merge Sort"""
# ยังไม่เสร็จนะไอดำ
def main():
    """main"""
    num = []
    while True:
        x = input()
        if x == "END":
            break
        num.append(int(x))
    if len(num) < 2:
        print(*num)
    else:
        left = num[:len(num) // 2]
        right = num[len(num) // 2:]
        print(left)
        print(right)
main()
