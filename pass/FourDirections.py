"""FourDirections"""
def main():
    """main"""
    x = input()
    for i in range(5):
        ans = ""
        for j in x:
            if i in (0, 4) or ((i == 3 and j == "U") or (i == 1 and j == "D")):
                ans += "  *   "
            if (i == 1 and j == "U") or (i == 3 and j == "D"):
                ans += " ***  "
            if i == 2 and j in ("U", "D"):
                ans += "* * * "
            if i == 2 and j in ("L","R"):
                ans += "***** "
            if i in (1, 3) and j == "L":
                ans += " *    "
            if i in (1, 3) and j == "R":
                ans += "   *  "
        print(ans)
main()
