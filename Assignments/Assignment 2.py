# 1. Print out the following text: # You've reached [your name]. # I'm not available right now, so leave a message and I'll call you back.

# 2. Create five variables for your first name, last name, shoe size, height, and age. # And then print them out on one line.

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount# in a variable named total and print it out.

# 4. Convert 158.8 into an integer. # Convert 75 into a float. # Convert "244.9" into a float and then an integer.

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:# -in the woods#               which#                   stutter#                           and# #                               sing

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: # Mattan, your total is $12.91 # (remember to round the total to the nearest cent)

# 7. Use input() to ask a user for the city they live in, and then print it back tothem.

# 8. Build a future value calculator by using input() to get values from the user. # (Make sure you convert them into integers or floats before doing any math on them.) # Print out the result.# Hint: Future Value = Present Value x (1 + rate of return) ^ number of
import math

print('Question 1')

# Here I am creating a variable for my name

your_name = 'Adrian A. Greaves'

# Here I am printing out a text message using the print() function and a f-string literal string with an expression\n with an expression in curly braces...ex: {your_name} 

print(f"You've reached {your_name}. I'm not available right now, so leave a message and I'll call you back.")
print('\n')


print('Question 2')
# Here I am creating five variables for my first & last name, my shie size, my height & weight

first_name = 'Adrian'
last_name = 'Greaves,'
shoe_size = '14,'
height = "6'3,"
age = '45\n'

print(first_name + " " + last_name + " " + shoe_size + " " + height + " " + age)
# I tried to print this question another
# Here I created another variable all my vitals and used an f-string to replace all the the variables I created
vitals = f"{first_name} {last_name} {shoe_size} {height} {age}"
print(vitals)
print('\n')


print('Question 3')
subtotal = 10.58
tip = 0.22
total = subtotal * tip + subtotal
print(total)
print('\n')


print('Question 4')
# Here I am converting 158.8 into an integer, 75 into a float and the string "244.9" into a float and then an integer.
print(int(158.8))
print(float(75))
print(float("244.9"))
print(int(float("244.9")))
print('\n')


print('Question 5')

text = '-in the woods\n\t\t which\n\t\t\tstutter\n\t\t\t\t and\n\n\t\t\t\t\t sing'
print(text)
print('\n')


print('Question 6')

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: # Mattan, your total is $12.91 # (remember to round the total to the nearest cent)
total = 12.91
print(f"{first_name}, your total is ${round(total, 1)}")
print('\n')



print('Question 7')

city = input("What city do you live in?: ") 
print(city)
print('\n')


print('Question 8')


FV = 'Future Value'

PV = float(int(input('Please enter the present value: ')))


r = float(input('Please enter the monthly intrest rate: '))
r = r/100

n = float(input('Please enter the number of months the money will be left in the account: '))

FV = PV*(1+r)**n

print(f"An account with a Present Value of ${PV:.2f} at a {r}% monthly interest rate left in an account for {n}\nmonths will earn you a Future Value of ${round(FV, 2)}")
print('${:.2f}'.format(FV))
print('\n')



# >>> '${:.2f}'.format(cash)
# '$3.40'
# >>> values = [1.2, 65.32, 15.2345]
# >>> template = 'Stuff costs ${:.2f}.'
# >>> for value in values:
#         print(template.format(value))