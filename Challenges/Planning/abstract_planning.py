# shopping list data structure
# a list (whole shopping cart), and inside the list create a dictionary for each type of
# each item in the cart has a name(string), quantitiy (interger) price(float)

cart1 = [{'name': 'milk (gallon)', 'quantity': 3, 'price': 5.99},
		 {'name': 'dawn dish soap', 'quantity': 1, 'price': 2.99}]


# a dictionary (whole shopping cart), inside the dictionary make an inner dictionary for
# outer dictionary - cart
# inner dictionary - item in cart

cart2 = {'milk (gallon)': {'quantity': 1, 'price': 5.99},
		  'dawn dish soap': {'quantity': 1, 'price': 2.99}}



# Plan ahead how to get the totl price of the shopping cart

# List version

def get_total_list(cart):
	pass
	# initialize total price to 0 (guardian)
	total_price = 0
	# iterate through all the items, and for each item
	for item in cart:
		# multiply the quantity by the price - add that to the total_price
		total_price == item['quantity'] * item['price']
	# return the total price
	return(total_price)


cart1_total = get_total_list(cart1)	
print(cart1_total)

#DICTIONARY VERSION (for cart 2 only)

def get_total_dictionary(cart):
	# initiliaze total price to 0
	total_price = 0
	# get the keys for all items in the dictionary (each key stands for one item)
	# put them into a list
	cart_items_names = list(cart.keys())

	# for each of the inner dictionaries
	for name in cart_items_names:
		# # multiply the quantity by the price - add that to the total_price
		total_price+= cart[name]['quantity']*cart[name]['price']
	# return the total price
	return total_price

cart2_total = get_total_dictionary(cart2)
print(cart2_total)
