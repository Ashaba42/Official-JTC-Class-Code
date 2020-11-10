# 1. Write an if statement that checks if user is "mattangriffel"# and prints out "Welcome professor" if so, or "Who are you?" if not.user = "mattangriffel"

mattangriffel = True
user = input('Name please: ')

if user == 'mattangriffel':
	print('Welcome professor')
else:
	print('Who are you?')	


# 2. Write an if statement that checks both the credentials below# and prints "Successfully logged in." if they're correct or# "Invalid username/password combination. Try again." if they're not.user = "mattangriffel"password = "123456"

print('Please enter correct username and password combo to continue')

username=input('Enter username: ')
password=input('Enter password: ')

if username == 'mattangriffel' and password == '123456':
	print('Successfully logged in.')
else:
	print('Invalid username/password combination. Try again.')
print('Please enter correct username and password combo to continue')


# 3. Write an if statement that checks whether the value of number is divisible# by two and prints out "even" if it is and "odd" if it's not.# (Hint: You can check divisiblity using the modulus (%) operator. # n % k == 0 evaluates to true if n is an exact multiple of k.)number = 4

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# 4. Create three different lists containing:# - The names of all your siblings# - Your top 3 favorite movies# - The latitude and longitude coordinates of Columbia University

siblings = ['Carry', 'Anthony']

favorite_movies = ['Jaws', 'Batman', 'Captain America: Winter Soldier']

latitude_longitude_Columbia_University = ['40.8045 Lat', '-73.9572 Lon']


# 5. Use a for loop on each of the lists above to print out each element on its ownline.

for sibling in siblings:
	print(sibling)

for movie in favorite_movies:
	print(movie)	

for location in latitude_longitude_Columbia_University:
	print(location)


# 6. Use a for loop and the title() function to print out each city name capitalizedcities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]

cities = ['new york city', 'san francisco', 'boston', 'chicago', 'los angeles']
for city in cities:
	c = city.title()
	print(c)

# 7. A list is different from an element in a list.  What's something you can do# to the second in Python that you can't do to the first, and vice versa?person = ["Mattan"]person = "Mattan"

#### Answer === # person = ["Mattan"], is considered a list in Python and the values in a list can be altered even after its creation
			    
			    # As for person = "Mattan", it is considered to be a container in Python that contains a value...once created, one can't change it's value however, one can reassign the original value with a new value


# 8. Use range() and a for loop to print out:# - the numbers from 1 to 10# - the square of each of the numbers from 1 to 10# - for each number from 1 to 10, print out whether it is even or not

for num in range(1, 11):
	print(num)

for num in range(1, 11):
	square_all = num ** 2
	print(square_all)

start, end = 1, 10
for num in range(start, end + 1):
	if (num % 2) == 0:
   		print("{0} is Even".format(num))
	else:
   		print("{0} is Odd".format(num))        

#  Bonus: In Mathematics, a Marsenne number is a number that is one less than a# power of two (i.e. 2^n - 1). Starting with an empty list named # marsenne_numbers (provided for you below),  use the append() function inside# of a for loop so that after the loop has run, marsenne_numbers contains a# list of the first ten Marsenne numbers.
# marsenne_numbers = []

mersenne_numbers = []

print('Here are the ten numbers: ')
for num in range(1, 11):
	n = 2**num-1
	mersenne_numbers.append(n)
	print(n)