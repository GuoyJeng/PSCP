"""a"""
ax, ay, aw, ah = list(map(int, input().split()))
bx, by, bw, bh = list(map(int, input().split()))

overlap_width = max(0, min(ax + aw, bx + bw) - max(ax, bx))
overlap_height = max(0, min(ay + ah, by + bh) - max(ay, by))
overlap_area = overlap_width * overlap_height

if overlap_area > 0:
    print(overlap_area)
else:
    print("no overlapping")
