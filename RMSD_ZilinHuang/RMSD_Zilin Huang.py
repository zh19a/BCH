#!/usr/bin/env python
#Zilin Huang
#Github address: https://github.com/zh19a/lingyu/tree/master/RMSD_ZilinHuang
from math import sqrt

# define function to read file and extract data
def readfile(x):
	# read file
	f = open(x,'r')
	lines = f.readlines()
	f.close
	atoms = []
	# extract data
	for line in lines:
		words = line.split()
		if words[0] == "ATOM":
			words[1] = int(words[1])
			words[6] = float(words[6])
			words[7] = float(words[7])
			words[8] = float(words[8])
			atoms.append(words)
	return atoms

# define function to calculate RMSD in two pdb files
def RMSDcal(x,y):
	i = 0
	j = 0
	n = 0
	RMSD2N = 0.0
	while i+1 <=len(x) and j+1 <= len(y):
		### calculate RMSD beginning with same line
		if x[i][1] == y[j][1] and x[i][11] == y[j][11]:
			RMSD2N += (x[i][6]-y[i][6])**2+(x[i][7]-y[i][7])**2+(x[i][8]-y[i][8])**2
			i += 1
			j += 1
			n += 1
					
	return sqrt(RMSD2N/n)

f1 = readfile('2FA9noend.pdb')
f2 = readfile('2FA9noend2mov.pdb')
RMSD = RMSDcal(f1,f2)
print ("RMSD of two pdb files is: ", RMSD)





