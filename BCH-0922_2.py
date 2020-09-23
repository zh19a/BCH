#coding=utf-8

import numpy as np
import math
import sys

print("Enter A,B,C coordinates in the form: A_x A_y B_x B_y C_x C_y ")
input_coord = sys.stdin.readline()
split_input = str.split(input_coord)
A_x = float(split_input[0])
A_y = float(split_input[1])
B_x = float(split_input[2])
B_y = float(split_input[3])
C_x = float(split_input[4])
C_y = float(split_input[5])

diff_AB_x = math.fabs(B_x - A_x)
diff_AB_y = math.fabs(B_y - A_y)

diff_AC_x = math.fabs(C_x - A_x)
diff_AC_y = math.fabs(C_y - A_y)

diff_BC_x = math.fabs(C_x - B_x)
diff_BC_y = math.fabs(C_y - B_y)

lenAB = math.sqrt(math.pow(diff_AB_x, 2) + math.pow(diff_AB_y, 2))
lenAC = math.sqrt(math.pow(diff_AC_x, 2) + math.pow(diff_AC_y, 2))
lenBC = math.sqrt(math.pow(diff_BC_x, 2) + math.pow(diff_BC_y, 2))

pi180 = 180 / math.pi

cosA = (lenAC**2 + lenAB**2 - lenBC**2) / (2 * lenAC * lenAB)
cosB = (lenBC**2 + lenAB**2 - lenAC**2) / (2 * lenBC * lenAB)
cosC = (lenAC**2 + lenBC**2 - lenAB**2) / (2 * lenAC * lenBC)

A = str(math.acos(cosA) * pi180)
B = str(math.acos(cosB) * pi180)
C = str(math.acos(cosC) * pi180)

sys.stdout.write("angle A: " + A + '\n' + "angle B:" + B + '\n' + "angle C: " + C + '\n')







