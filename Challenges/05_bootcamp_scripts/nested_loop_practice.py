# loops inside loops
days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

# outer loop
for day in days:
	print(day)
	# for each day, print each letter individually
	# inner loop
	for letter in day:
		print(letter)

# not nested, put prints first letter of each day
for day in days:
	print(day)
	print(day[0])

# outer loop
for day in days:
	print(day)
	# for each day, print each letter individually
	# inner loop
	for letter in day:
		print(letter.upper())


# nested loops with range()
for outer_var in range(3):
	for inner_var in range(4):
		print(f'outer: {outer_var}, inner: {inner_var}')


# multiple loops, no nesting
for outer_var in range(3):
	print(f'outer: {outer_var}')
for inner_var in range(4):
	print(f'inner: {inner_var}')

# printing the looping variable after the loop is done
print(inner_var)
print(inner_var)
print(inner_var)
print(inner_var)

# logic inside loops
days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

# loop through days, print whether it's weekend or not

for day in days:
	#if the day variable starts with s
	if day.startswith('s'):
		print(f'{day} is a weekend')
	else:
		print(f'{day} is a weekday')

# XTREME NESTING
# loop through days, print whether it's weekend or not
# if it is a weekday, print 'contains o' if th letter o is in the day
for day in days:
	#if the day variable starts with s
	if day.startswith('s'):
		print(f'{day} is a weekend')
	else:
		print(f'{day} is a weekday')
		if 'o' in day:
			print('contains o')
		else:
			print('no o')

# break 'breaks you out of the loop'

for day in days:
	print(day)
	if day.startswith('w'):
		break
print('done with loop')