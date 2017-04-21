"""
Written by: Shreyas Daniel - github.com/shreydan
Description: an overview of 'timy' module - pip install timy

A great alternative to Pythons 'timeit' module and easier to use.
"""

import timy # begin by importing timy

@timy.timer(ident = 'listcomp', loops = 1) # timy decorator
def listcomprehension(): # the function whose execution time is calculated.
	li = [x for x in range(0,100000,2)]

listcomprehension()

"""
this is how the above works:
	timy property is created.
	any function underneath the timy decorator is the function whose execution time
	need to be calculated.
	after the function is called. The execution time is printed.
	in the timy decorator:
		ident: an identity for each timy property, handy when using a lot of them
		loops: no. of times this function has to be executed
"""

# this can also be accomplished by 'with' statement:
# with tracking points in between code.

def listcreator():
	with timy.Timer() as timer:
		li = []
		for i in range(0,100000,2):
			li.append(i)
			if i == 50000:
				timer.track('reached 50000')

listcreator()

"""
there are many more aspects to 'timy' module.
check it out here: https://github.com/ramonsaraiva/timy 
"""