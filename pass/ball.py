"""FOR!F-Ball"""
def main():
    """main"""
    x = input()
    ball = 1
    for i in x:
        if i == "A":
            if ball == 2:
                ball = 1
                continue
            if ball > 2:
                continue
            ball = 2
        elif i == "B":
            if ball == 3:
                ball = 2
                continue
            if ball < 2:
                continue
            ball = 3
        elif i == "C":
            if ball == 3:
                ball = 1
                continue
            if ball == 2:
                continue
            ball = 3
    print(ball)
main()
