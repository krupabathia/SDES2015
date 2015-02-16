from text_plot import *

def test_move():
	movetowithoutenter(4,10)
	
def check_lengthmismatch():
	x = [100,200,300,400]
	y = [1,2,3,4,5]
	plot_variableresolution(x,y,10,10)
	
	
def check_sortbyy():
	x = [1,2,3,4,5]
	y = [10,0,2,5,15]
	sortbyy(x,y)
	
def check_plot():
	x = [1,2,3,4,5]
	y = [1,2,3,4,5]
	plot(x,y)
	
def check_scaling():
	x = [1,2,3,4,5]
	resolution = 5
	scale(x,resolution)
	
def drawing_square():
	x = [1,2,3,4,5,5,5,5,5,4,3,2,1,1,1,1]
	y = [1,1,1,1,1,2,3,4,5,5,5,5,5,2,3,4]
	plot_variableresolution(x,y,15,15)
	
'''test_move()
check_lengthmismatch()
check_sortbyy()
check_plot()
check_scaling()'''
drawing_square()
