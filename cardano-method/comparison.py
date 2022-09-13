
from cubic import CubicEquation
import time
import numpy as np
import random

# table with three columns -> numpy time, cardano method time, numpy output, cardano output

def makeComparison(coeff):
    try:
        # CubicEquation
        start = time.time()
        first_roots = CubicEquation(coeff)
        first_time = time.time() - start

        # NumPy
        start = time.time()
        second_roots = np.roots(coeff)
        second_time = time.time() - start
        return first_time, second_time
    except:
        return -1, -1

def testing(num_iter):
    print(f"calculating with {num_iter} iterations...")
    my_results = []
    numpy_results = []
    for _ in range(num_iter):
        four_num = [random.randint(1, 10000) for __ in range(4)]
        comparison = makeComparison(four_num)
        if comparison[0] != -1:
            my_results.append(comparison[0])
            numpy_results.append(comparison[1])
    return sum(my_results)/len(my_results), sum(numpy_results)/len(numpy_results)

final_times = []

for i in range(4):
    final_times.append(testing(10 ** (i+1)))

for i in range(4):
    print(final_times[i][1]/final_times[i][0], '{:f}'.format(final_times[i][0]), '{:f}'.format(final_times[i][1]))