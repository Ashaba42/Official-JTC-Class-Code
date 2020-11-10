# write a function that takes the average of numbers in a list
def average(number_list):
	# 'pass'n is a placeholder: othing happens in this function
	pass

	# get the sum of the numbers in number_list
	number_sum = sum(number_list)

	# divide the sum by the length of number_list
	list_average = number_sum / len(number_list)

	# return the average
	return list_average

# run the function
my_list = [1,2,3,4]
my_average = average(my_list)
print(my_average)



# Make aanother function
# Decide wheather I should wear a jacket today

def should_wear_jacket(temp):
	# if temp is below 60 degrees
		# print ot 'wear jacket'
	# otherwise
		# print out 'no jacket needed'
	pass	

def should_wear_jacket(temp):
	# if temp is below 60 degrees
	if temp < 60:
		# print ot 'wear jacket'
		print('Wear a jacket')
	# otherwise
	else:
		# print out 'no jacket needed'
		print('No jacket needed')

# run the function
should_wear_jacket(23)		

# creating email addresses
names = ['Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', 'Adrian Greaves', ]

# make a function that turns the names into email addresses

def make_email_ids(names_list):
	pass

	# create an output list to pull the email addresses in

	# for every name in the list
		# split the name into 2 strings woth a space
		# join first and last name together with a dot in between
		# make the names lower case
		# add @gmail.com to the name
		# add (append) the email address to the output list

	# return the output list


def make_email_ids(names_list):
	# create an output list to pull the email addresses in
	output_list = []
	# for every name in the list
	for name in names_list:
		# split the name into 2 strings woth a space
		split_names = name.split(' ')
		# join first and last name together with a dot in between
		join_names = '.'.join(split_names)
		# make the names lower case
		lower_names = join_names.lower()
		# add @gmail.com to the name
		email = lower_names + '@gamil.com'
		# add (append) the email address to the output list
		output_list.append(email)

	# return the output list
	return output_list


emails = make_email_ids(names)
print(emails)