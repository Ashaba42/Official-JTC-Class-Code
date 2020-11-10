# # the syntex

# # for loop
# # numbers = [12, 8, 41]

# # for num in numbers:
# # 	print(num)
# # 	print('hello world')
# # # for loop done
# # print('hi, computer!')

# # complicated operations in loops

# # lower case strings
# lower_list = 'here', 'are', 'my', 'lower', 'case', 'words'
# upper_list = []


# # print(dir(lower_list))


# # for i in lower_list:
# # 	upper_list.append(i.upper())

# # print(upper_list)

# # mixed data types
# mixed = [23, 'word', 23.4, True]
# data_types = []

# for data in mixed:
# 	data_types.append(type(data))
# 	print('iteration', data, data_types)
	
	

# # for loop is done, run the test
# print('independent print', data_types)


# my_string = 'ice cream'
# vowels = ['a', 'e', 'i', 'o', 'u']


# for char in my_string:
# 	# if char in vowels:
# 	# 	print(f'{char} is a vowel')
# 	# else:
# 	# 	print(f'{char} is a not a vowel')

# 	# if char == ' ':
# 	# 	print(f'{char} is a space')
# 	# if char in vowels:
# 	# 	print(f'{char} is a vowel')
# 	# else:
	# 	print(f'{char} Nothing to see here!')

# range() takes a number -> iterate a many times as number
# len(lower_list) used to determine the number of items in a list

# lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']

# # uppper_list = []

# for i in range(len(lower_list)):
# 	lower_list[i] = lower_list[i].capitalize()

# print(lower_list)


# while loops

count = 0

while count < 5:
	# code block
	# as long as condition is True, it will run code
	print('iteration', count)
	count = count + 1

print('done', count)
