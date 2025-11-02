"""a"""
s = input()

tokens = []
cur = []
INSIDE = False
i = 0

while i < len(s):
    ch = s[i]
    if INSIDE:
        if ch == ">":
            INSIDE = False
        i += 1
        continue
    if ch == "<":
        if cur:
            tokens.append("".join(cur))
            cur = []
        INSIDE = True
        i += 1
        continue
    if ch.isspace():
        if cur:
            tokens.append("".join(cur))
            cur = []
    else:
        cur.append(ch)
    i += 1

if cur:
    tokens.append("".join(cur))

print(tokens)
