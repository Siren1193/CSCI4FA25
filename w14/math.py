import math
#| x1 - x2 |^2 + |y1 - x2 |^2 = c^2

x1 = 5
y1 = 6

x2 = -5
y2 = -6

point1 = [x1,y1]
point2 = [x2,y2]

absx = abs(x1 - x2)
absy = abs(y1 - y2)

print(absx)
print(absy)

print(math.hypot(absx,absy))
