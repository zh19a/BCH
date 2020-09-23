#coding=utf-8


import sys
import numpy as np
import math

print("Enter temp in degrees Fahrenheit: ")
F = float(sys.stdin.readline())
print("Temp in degrees Fahrenheit is : ", F )

K = str((F + 459.67) * (5/9))

sys.stdout.write("Temp in degrees Kelvin is : " + K + '\n')




















