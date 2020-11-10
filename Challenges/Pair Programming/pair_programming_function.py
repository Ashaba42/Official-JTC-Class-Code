# creating account 
def create_account():
	username = input('Please enter your name: ')
	password = input('Please enter your password: ')

	account = {'username': username, 'password': password, 'balance': 0.00 }

	return account 

# define a deposit function
def deposit(account, amount):
	# print(account['balance'])
	account['balance'] += float(amount)   
	print(f'{account["username"]} deposited, {amount}')
	print(account['balance'])

# define a withdraw function
def withdraw(account, amount):
	if amount <= account['balance']:
		account['balance'] -= amount
		print(account['balance'])
	else: 
		print(f'Insufficient funds! Only ${account["balance"]} available')

# BONUS
# password protected version
def validate(account, attempts = 0):
	# logged_in = False
	# while logged_in == False:
	# 	print('Validating account info:')
	username = input('Enter username: ')
	password = input('Enter password: ')
	if username == account['username'] and password == account['password']:
		# logged_in = True
		print('Logged in!')
	else:
		print('Incorrect username/password combo')
		attempts +=1
		print(attempts)
		if attempts < 3:
			validate(account, attempts)
		else:
			print('Sorry, you are locked out of your account. Please call your bank representative.')	
			quit()

# secure version of functions
def deposit_secure(account, amount):
	validate(account)
	deposit(account, amount)
	# account['balance'] += amount

def withdraw_secure(account, amount):
	validate(account)
	withdraw_secure(account, amount)
	# if amount == account['balance']:
	# 	account['balance'] += amount
	# else:
	# 	print(f'Insufficient funds! Only ${account["balance"]} available')
		