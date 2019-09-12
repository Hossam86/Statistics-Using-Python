# https://www.w3resource.com/python-exercises/math/python-math-exercise-57.php
import math

def sd_calc(data):
    n = len(data)

    if n <= 1:
        return 0.0
    mean, sd = avg_calc(data), 0.0
    # calc stan. dev,

    for el in data:
        sd += (float(el)-mean)**2
    sd = math.sqrt(sd/float(n-1))

    return sd


def avg_calc(ls):
    n, mean = len(ls), 0.0
    if n <= 1:
        mean = ls[0]

    # calculate the average
    for el in ls:
        mean = mean+float(el)
    mean = mean/n
    return mean


data = [4, 2, 5, 8, 6]
print("Sample Data", data)
print("Standard Deviation : ", sd_calc(data))
