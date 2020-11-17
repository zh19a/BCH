#!/usr/bin/env python
#Zilin Huang
#Github Address: 


import numpy as np
from math import sqrt
from matplotlib import pyplot

def peakfinding(x):
	f=open(x,'r')
	lines=f.readlines()
	f.close()


# extracting data 
	times=[]
	heights=[]
	z=0
	for line in lines[3:]:
		words=line.split()
		# excluding fisrt three and last blank line
		if len(words)>1:
				times.append(float(words[0]))
				heights.append(float(words[1]))


# loop for calculating baseline 
# method:exclude data > the threshhold, recalculate mean until standard deviation is smaller than the threshhold 10
# restheights: data without the excluded data
	restheights=heights[:]
	threshhold=10
	# sd()return the standard deviation of list restheights
	while sd(restheights)>threshhold:
		h=np.array(restheights)
		ha=h.mean()
		i=0
		# delete elements larger than the set average + meandif 
		while  i < len(restheights):
			if restheights[i]-threshhold>ha:
				del restheights[i]
				continue
			i+=1
	baseline=np.array(restheights).mean()


# loop to find peaks
# method:peak starts when height reaches baseline+linedif, and ends when reaching a lowest point in that small region or fall below the line set above.	
	# peaks: a list of list of list.
	peaks=[[[]]]+[[[]]]
	# p: peak number
	p=0
	i=1
	while i+1< len(times):
		# peak begin, 3*sd is used after severl attempts 
		while heights[i]>baseline+3*sd(restheights):
			peaks[0][p].append(times[i])
			peaks[1][p].append(heights[i])
			# peak end,  when a point reaches a lowest point or height drops to normal line, jump out to append, then add new list into peaks[0] and peaks[1]
			if heights[i-1]>heights[i] and heights[i]<heights[i+1] or heights[i+1]<=(baseline+3*sd(restheights)):
				peaks[0]=peaks[0]+[[]]
				peaks[1]=peaks[1]+[[]]
				p+=1
				break
			i+=1
		i+=1
# peaks data are stored in list


# loop to print the maximum absorbance and plot peaks
	num=0
	color={0:'go',1:'yo',2:'ro',3:'bo'}
	while num+1<len(peaks[0]):
		begin=peaks[0][num][0]
		end=peaks[0][num][-1]
		a=np.array(peaks[1][num])
		maximum=a.max()
		tp=peaks[0][num][a.argmax()]
		### begin/end:begin/end point of peak tp: time of maximum
		print ("peak%3d  begins at %8.3f, end at %8.3f, with maximum absorbance %8.3f at time %8.3f" %((num+1),begin,end,maximum,tp))
		pyplot.plot(peaks[0][num],peaks[1][num],color[num])
		num+=1

		pyplot.plot(times,heights,'k:')
		pyplot.show()


# define a function sd for calculating the standard deviation in a list
def sd(x):
	a=np.array(x)
	mean=a.mean()
	sd2=0.0
	for n in x:
		sd2+=(n-mean)**2
	sd=sqrt(sd2/len(x))
	return sd

peakfinding("superose6_50.asc")
