"""progressivetax"""
NUM = int(input())
A = (300000 - 150000) * 0.05
B = (500000 - 300000) * 0.1
C = (750000 - 500000) * 0.15
D = (1000000 - 750000) * 0.2
E = (2000000 - 1000000) * 0.25
F = (4000000 - 2000000) * 0.3

if 0 <= NUM <= 150000:
    print(0)
elif 150000 < NUM <= 300000:
    NUM -= 150000
    NUM *= 0.05
    print(int(NUM))
elif 300000 < NUM <= 500000:
    a1 = (NUM - 300000) * 0.1
    print(int(a1 + A))
elif 500000 < NUM <= 750000:
    a1 = (NUM - 500000) * 0.15
    print(int(a1 + A + B))
elif 750000 < NUM <= 1000000:
    a1 = (NUM - 750000) * 0.2
    print(int(a1 + A + B + C))
elif 1000000 < NUM <= 2000000:
    a1 = (NUM - 1000000) * 0.25
    print(int(a1 + A + B + C + D))
elif 2000000 < NUM <= 4000000:
    a1 = (NUM - 2000000) * 0.3
    print(int(a1 + A + B + C + D + E))
elif NUM > 4000000:
    a1 = (NUM - 4000000) * 0.35
    print(int(a1 + A + B + C + D + E + F))
