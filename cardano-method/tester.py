
from cubic import CubicEquation
import time
import numpy as np
import random

# table with three columns -> numpy time, cardano method time, numpy output, cardano output

def makeComparison(coeff):
    # CubicEquation
    start = time.time()
    first_roots = CubicEquation(coeff).solve()
    first_time = time.time() - start

    # NumPy
    start = time.time()
    second_roots = np.roots(coeff)
    second_time = time.time() - start
    return first_time, second_time

avg_time = ''
results = []

for _ in range(100):
    four_num = [random.randint(1, 10000) for __ in range(4)]
    comparison = makeComparison(four_num)
    results.append(comparison[0]/comparison[1])

print(results)

print(sum(results)/len(results))
