import numpy as np

a = 1
b = 2
sum = 0
total = 0
while sum <= 4000000: 
    sum = a + b
    a = b
    b = sum 
    if a%2 == 0:
        total+=a
print(total)