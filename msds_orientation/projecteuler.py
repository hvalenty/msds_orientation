import numpy as np

list = np.array([3,4,5,6,7,8,9])
for num in list:
    if num%3==0 or num%5==0:
        total = sum(num)

print(total)