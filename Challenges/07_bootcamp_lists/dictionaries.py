# dictionaries

#blank_dict = {}
#print(type(blank_dict))

#user_account_as_list = ['agreaves', 270.26]

username = 'agreaves'
balance = 270.26


user_account = {
	'username': 'agreaves', #--key and value
	'balance': 270.26
}

# adding a new value
user_account['last_transaction_date'] = '9/15/2020'

#print(user_account['last_transaction_date'])
#print(user_account['balance'])

user_account['user_birthyear'] = 1993

#print(user_account)

# reassigning a value to a key
user_account['balance'] = 500.00

#print(user_account)

# remove a key value pair
user_account.pop('user_birthyear')

#print(user_account)


# lists vs dictionaries
groceries = ['apples', 'bananas', 'cherries']
#print(groceries[1])

groceries_dict = {
	'fruits': ['apples', 'bananas', 'cherries'],
	'vegetables': ['carrots', 'parsley']
}
#print(groceries_dict['fruits'])

#print(groceries_dict['fruits'] + groceries_dict['vegetables'])
#print(groceries_dict)


#nums = 100, 200 300, 400, 500, 600
#print(nums[0], nums[2], nums[4])

print(user_account['username'], user_account['balance'])

