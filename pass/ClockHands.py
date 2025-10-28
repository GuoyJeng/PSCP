"""a"""
HOUR_STEP = 5.0
TOTAL_TICKS = 60.0
ONE_TICK = 1.0

h = int(input().strip())
m = int(input().strip())

hour_pos = (h % 12) * HOUR_STEP + m / 12.0
min_pos = float(m)

diff = hour_pos - min_pos
if diff < 0:
    diff += TOTAL_TICKS

print("True" if diff < ONE_TICK else "False")
