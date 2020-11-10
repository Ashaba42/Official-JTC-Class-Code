# os library							# best practice to always import library at top
import os			

# importing a library and set alias (rename)
import numpy as np

from custom_functions import say_hello
from custom_functions import fahrenheit_to_celcius
from custom_functions import *			# using this symbol allows you to import all the functions from this file

# from library to import a specific function
# from numpy import arange

# using an os function
# os.system('ls -l')
# os.system('mkdir dre')

# using np
# num_list = [5,7,9,12,200]
# # calculatee the mean
# list_average = np.mean(num_list)
# print(list_average) 

# # generate numbers list
# more_nums = np.arange(50)
# print(more_nums)



say_hello('Rob')
converted_temp = fahrenheit_to_celcius(70)
# print(fahrenheit_to_celcius(70))
print(converted_temp)


# make an array of intergers between 70 and 80
temps_f = np.arange(70, 80)
print(temps_f)
# print(type(temps_f))
# print(type({}))

# loop over each temp and convert it to celcius
for f in temps_f:
	# fahrenheit_to_celcius(f)
	c = fahrenheit_to_celcius(f)
	print(f'{f} fahrenheit is {c} celcius')
	# print(f) 