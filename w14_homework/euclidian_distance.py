#finding the euclidean distance in python
import math

x1 = 5
y1 = -56

x2 = -5
y2 = 99

absx = abs(x1 - x2)
absy = abs(y1 - y2)

Pythag_A = int(absx)
Pythag_B = int(absy)

print(math.hypot(absx,absy))

