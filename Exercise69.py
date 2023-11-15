approximation = 3.0
sign = 1  
for i in range(1, 16):
    denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
    term = 4 / denominator * sign
    approximation += term
    sign *= -1  # Change the sign for each term

    print(f"Approximation {i}: {approximation}")

import math
print(f"\nActual value of π: {math.pi}")
