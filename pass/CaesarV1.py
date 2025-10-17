"""CaesarV1"""
def main():
    """main"""
    num = int(input())
    word = input()
    ans = ""
    for i in word:
        if i.islower():
            ans += chr((ord(i) - ord("a") + num) % 26 + ord("a"))
        elif i.isupper():
            ans += chr((ord(i) - ord("A") + num) % 26 + ord("A"))
        else:
            ans += i
    print(ans)
main()
