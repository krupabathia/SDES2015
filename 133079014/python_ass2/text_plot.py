import math
import sys

#Plotting an '*' at a given co-ordinate
def movetowithoutenter(x,y):
	#print x,y
	for i in range(0,y):
		sys.stdout.write('\n')
	for i in range(1,x):
		sys.stdout.write(' ')
	sys.stdout.write('*')
	
#scaling the given list according to the terminal size
def scale(x,resolution):
	length = len(x)
	xmax = max(x)
	xscaled = []
	for i in range(0,length):
		xscaled.append(x[i]*resolution/xmax)
	return xscaled
	
#plotting with variable resolution
def plot_variableresolution(x,y,xres,yres):
	xlen = len(x)
	ylen = len(y)
	try:
		if xlen != ylen:
			raise ValueError
		elif type(xres) is not int:
			raise TypeError
		elif type(yres) is not int:
			raise TypeError
		xscaled = scale(x,xres) #xres refers to the no of columns on the screen
		yscaled = scale(y,yres) #yres refers to the no of rows on the screen
		sortedx,sortedy = sortbyy(xscaled,yscaled)
		for i in range(0,xlen):
			if i != 0:
				movy = abs(sortedy[i]-sortedy[i-1])
				if movy == 0:
					movx = abs(sortedx[i]-sortedx[i-1])
					movetowithoutenter(movx, movy)
				else:
					movetowithoutenter(sortedx[i], movy)
			else:
				movetowithoutenter(sortedx[i],sortedy[i])
		print '\n'
	except ValueError:
		print "The no of elements in x and y lists/tupple should be equal"
	except TypeError:
		print "Enter integer no of rows/columns"
	

#plotting with default screen resolution
def plot(x_i,y_i):
	plot_variableresolution(x_i,y_i,80,30)
	

#default plot - i.e plotting a sine wave
def default_plot():
	length = 80
	yres = 30
	unitx = (2*math.pi)/length
	xlist = []
	yinit = []
	sortedx = []
	sortedy = []
	for i in range(0,length):
		xlist.append(i)
		k = unitx*i
		yi = math.sin(k)
		y1 = (yi - 1)
		if y1 != 0:
			y2 = int(y1*(-yres/2))
		else:
			y2 = int(y1)
		yinit.append(y2) #obtain the values of the sine function
	sortedx, sortedy = sortbyy(xlist,yinit)
	for i in range(0,length):
		if i != 0:
			movy = abs(sortedy[i]-sortedy[i-1])
			if movy == 0:
				movx = abs(sortedx[i]-sortedx[i-1])
				movetowithoutenter(movx, movy)
			else:
				movetowithoutenter(sortedx[i], movy)
		else:
			movetowithoutenter(sortedx[i],sortedy[i])
	print '\n'
	

#sorting the values by y co-ordinates
def sortbyy(x,y):
	sortedx = []
	sortedy = []
	length = len(x)
	for i in range(0,length):
		index = y.index(min(y))
		sortedx.append(x[index])
		sortedy.append(min(y))
		x.remove(x[index])
		y.remove(min(y))
	for i in range(1,length):
		for i in range(1,length):
			if (sortedy[i] == sortedy[i-1]):
				if (sortedx[i] < sortedx[i-1]):
					sortedx[i],sortedx[i-1] = sortedx[i-1],sortedx[i]
	return sortedx,sortedy


if __name__ == '__main__':
	default_plot()
