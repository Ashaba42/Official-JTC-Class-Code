# Syntax Error
# print('hello world')

# Indentation Error
# def multiply(a, b):
# return a * b

# print(multiply(2, 3))	


# Tab Error
# def some_function():
# 	msg = 'hello world'
# 	print(msg)
# 	return msg

# some_function()


# Name Error
# a = b + 2
# square()

# Index Error
# groceries = ['apples', 'oranges', 'bananas']
# print(groceries[3])
# print(groceries[2])
# print(groceries[1])


# Type Error
# def square(num):
# 	return num * num

# print(square([]))


# try, except, else, finally

# try:
# 	# try running everything in this block
# 	print(groceries[1])
# except NameError:
# 	print('You did not define something in your try block')
# except:
# 	# if an error or exception arises in the try block, run this block
# 	print('There was something wrong')
# else:
# 	print('Runs when ther is no exceptions!')

try:
	# try running everything in this block
	print(groceries[1])
except:
	# if an error or exception arises in the try block, run this block
	print('There was something wrong')
else:
	print('Runs when there is no exceptions!')
finally:
	print('Always runs!')

