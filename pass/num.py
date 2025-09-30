"""Hee Yai Yai"""
num = int(input())
x = 1
c = 0
he = ''
while x <= num:
    c += x
    if x == 1:
        he += str(x)
    else:
        he += '+' + str(x)
    x += 1
print(he)
print(c)
