import numpy as np

num = 600851475143

for factor in range(2, num):
    if num%factor == 0 and num/factor == factor:
        print(factor)