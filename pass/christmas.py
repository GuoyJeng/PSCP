"""heheha"""
LIGHT = input()
X = int(input())
R = "Red"
G = "Green"
B = "Blue"
ANS = ""
COUT = 2
COUT1 = 3
for i in range(1,X + 1):
    if LIGHT == "R":
        if i == 1:
            ANS += R
        elif i == COUT:
            ANS += " " + G
            COUT += 3
        elif i == COUT1:
            ANS += " " + B
            COUT1 += 3
        else:
            ANS += " " + R
    elif LIGHT == "G":
        if i == 1:
            ANS += G
        elif i == COUT:
            ANS += " " + B
            COUT += 3
        elif i == COUT1:
            ANS += " " + R
            COUT1 += 3
        else:
            ANS += " " + G
    elif LIGHT == "B":
        if i == 1:
            ANS += B
        elif i == COUT:
            ANS += " " + R
            COUT += 3
        elif i == COUT1:
            ANS += " " + G
            COUT1 += 3
        else:
            ANS += " " + B
print(ANS)
