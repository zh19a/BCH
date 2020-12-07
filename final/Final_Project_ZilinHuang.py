#coding=utf-8
#Zilin Huang
#github address: https://github.com/zh19a/lingyu/blob/master/final/Final_Project_ZilinHuang.py

import numpy as np
import sys
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#--------------------------------------#
###------   Sphere Definition  ------###
#--------------------------------------#	

def Sphere(pqrfilename):
	#read pqr file, which gives the lining atoms consist of pocket 
	pqrfile = open(pqrfilename,'r')
	lines = pqrfile.readlines()
	pqrfile.close()

	records = []
	xdata = []
	ydata = []
	zdata = []
	Disdata = []
	center = []
	xgeo = float(0)
	ygeo = float(0)
	zgeo = float(0)
	num = int(0)

	#Extract needed information
	for line in lines:
		record = line.split()
		records.append(record) 
		if record[0] == 'ATOM': 
			pocketnum = record[4]
		#Here, we only care about pocket No.1 
			if pocketnum == '1':
				num = int(num + 1)
				x = float(record[5])
				y = float(record[6])
				z = float(record[7])
				xdata.append(x)
				ydata.append(y)
				zdata.append(z)	
				#geometry center calculation	
				xgeo = float(xgeo + x)
				ygeo = float(ygeo + y)
				zgeo = float(zgeo + z)
		
	xgeo_ave = float(xgeo / num)
	ygeo_ave = float(ygeo / num)
	zgeo_ave = float(zgeo / num)
	center = [xgeo_ave,ygeo_ave,zgeo_ave]
	print("center:", center)

	#find out the minimum and maximal distance between center and lining atoms
	for i in range(len(xdata)):
		distance = np.sqrt(np.square(xdata[i]-xgeo_ave)+np.square(ydata[i]-ygeo_ave)+np.square(zdata[i]-zgeo_ave))
		Disdata.append(distance)
	#In my research project, the defined sphere's radius must be in the range of [radius_min, radius_max]
	radius_min = np.min(Disdata)
	radius_max = np.max(Disdata)
	print("minimum radius:", radius_min)
	print("maximal radius:", radius_max)

	#define a sphere based on radius and center
	u = np.linspace(0, 2 * np.pi, 100)
	v = np.linspace(0, np.pi, 100)
	#for sphere with radius_min
	x1 = radius_min * np.outer(np.cos(u), np.sin(v)) + center[0]
	y1 = radius_min * np.outer(np.sin(u), np.sin(v)) + center[1]
	z1 = radius_min * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]
	#for sphere with radius_max
	x2 = radius_max * np.outer(np.cos(u), np.sin(v)) + center[0]
	y2 = radius_max * np.outer(np.sin(u), np.sin(v)) + center[1]
	z2 = radius_max * np.outer(np.ones(np.size(u)), np.cos(v)) + center[2]

	#plot the 3D defined sphere and pocket
	fig = plt.figure()
	ax = Axes3D(fig)
	#plot pocket lining atoms with scatter
	ax.scatter3D(xdata,ydata,zdata, cmap='Blues') 
	ax.plot_wireframe(x1, y1, z1, rstride=10, cstride=10, color = 'g')
	ax.plot_wireframe(x2, y2, z2, rstride=10, cstride=10, color = 'r')
	plt.show()



#--------------------------------------#
###------NUMERICAL INTERGRATION------###
###---Integrate dF/dL to obtain △G----###
#--------------------------------------#

def Integration(datfilename): 
	#read fl.dat file 
	datfile = open(datfilename,'r')
	lines = datfile.readlines()[2:]
	datfile.close()

	G_Rie = 0
	Gs_Rie = []
	G_Tra = 0
	Gs_Tra = []
	dFdls = []
	records = []
	#Extract needed information
	for line in lines:
		record = line.split()
		records.append(record)
		dFdl = float(record[2])
		dFdls.append(dFdl)

	#Riemann_Sum
	#dl is set as 0.01
	for i in range(len(dFdls)-1):
		G_Rie += float(dFdls[i])*0.01
		Gs_Rie.append(G_Rie)
	#△G integrated by Riemann_Sum
	print("△G integrated by Riemann_Sum: ", G_Rie)	

	#Trapeziod integration
	#dl is set as 0.01
	for i in range(len(dFdls)-1):
		dFdl_new = (float(dFdls[i+1]) + float(dFdls[i])) / 2
		G_Tra += dFdl_new*0.01
		Gs_Tra.append(G_Tra)
	#△G integrated by Trapeziod integration	
	print("△G integrated by Trapeziod integration: ", G_Tra)	

	#Plot two Integration
	x = np.linspace(0,1,num=100)
	plt.xlabel('l value')
	plt.ylabel('Binding Free Energy △G')
	plt.plot(x, Gs_Rie, color = 'b', label = "Riemann Sum")
	plt.plot(x, Gs_Tra, color = 'y', label = "Trapeziod integration")
	plt.legend(loc='best')
	plt.show()

def openHTML(f, title):
    f.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
""")
    f.write("<head>\n")
    f.write("<title>%s</title>\n" % title)
    f.write("</head>\n")
    f.write("<body>\n")


def writeHTMLImage(f, title, imgpath):
    f.write('<p class="">%s</p>\n' % title)
    f.write('<img src="%s" />\n' % imgpath)


def closeHTML(f):
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()


if __name__ == "__main__":

	Sphere("1m48-chainA_pockets.pqr")
	Integration("fl.dat")
	f = open('final.html', 'w')
	openHTML(f, "final project")
	f.write("<h1>Sphere Definition and Free Energy Integration of Protein-Ligand Binding MD Simulation </h1>\n")
	writeHTMLImage(f, "Defined sphere should be in the range of these two spheres: ", 'Sphere.png')
	writeHTMLImage(f, "Two integration methods are pretty closed with each other: ", 'Integration.png')
	closeHTML(f)
	f.close()














