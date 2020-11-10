'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']
a = sorted(my_friends)	# w3schools.com is where I got the code
print(a)

# 1B. Comment your code in 1A to convince yourself you understand how it works
# The sorted() function returns a sorted list of the specified object.

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}
print(my_account.keys()) # geeksforgeeks.org

# 2B. Comment your code in 2A to convince yourself you understand how it works
# The keys() method returns a view object that displays a list of all the keys in a given dictionary.


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'
substring = "wood"
count = my_string.count(substring) # programiz.com

# print count
print("The count is:", count)
# This is also amother way of doing it using one line of code
print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works
# The count() method returns the number of occurrences of the substring in the given string.


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']
count = my_list.count('banana')				# programiz.com
print('The count of banana is:', count)		
# Print it out using one line of code
print(my_list.count('banana'))

# 4B. Comment your code in 4A to convince yourself you understand how it works
# The count() method returns the number of times the element to be counted appears in the list.


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')
import numpy as np

res = np.array(my_list) 				# journaldev.com
unique_res = np.unique(res) 
print(unique_res)

# Here I am using one line of code to print a random number
print(np.unique(my_list))

# 5B. Comment your code in 5A to convince yourself you understand how it works
# I will need to convert the list to NumPy array using numpy.array(list-name) and then use the numpy.unique() method to fetch the unique data items from the numpy array


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

import numpy as numpy 		
rand_num = np.random.normal(0,1,1)				# w3resource.com
print("Random number between 0 and 1:")
print(rand_num)


# 6B. Comment your code in 6A to convince yourself you understand how it works
# In order to gereate a random number between 0 and 1, I had to import Numpy and use the np.random.normal() function to generate a random number

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
