"""a"""
import json
xs = json.loads(input())
f = float(input())

res = {k: v for k, v in xs.items() if v >= f}
res = sorted(res.items(), key=lambda x: x[0])

if res:
    print("\n".join(f"{k}\t{v:.2f}" for k, v in res))
else:
    print("Nope")
