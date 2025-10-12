"""Merge Sort"""
def main(x):
    """main"""
    if len(x) < 2:
        return x
    left = x[:len(x) // 2]
    right = x[len(x) // 2:]
    main(left)
    main(right)
    l, r, check = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            x[check] = left[l]
            l += 1
        else:
            x[check] = right[r]
            r += 1
        check += 1

    while l < len(left):
        x[check] = left[l]
        l += 1
        check += 1

    while r < len(right):
        x[check] = right[r]
        r += 1
        check += 1
    return x

num = []
while True:
    ans = input()
    if ans == "END":
        break
    num.append(int(ans))
for i in main(num):
    print(i)
