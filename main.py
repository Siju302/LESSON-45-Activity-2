# empty dictionary
my_dict = {}

# dictionary wih integer keys
my_dict = {1: 'apple', 2: 'ball'}

# ditionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'Sijuade', 'age': 15}

# Output: Sijuade
print(my_dict['name'])
print(my_dict.get('age'))

# update value
my_dict['age'] = 16
print(my_dict)

# add item
my_dict['address'] = 'Uptown'
print(my_dict)

# remove particular element
my_dict.pop('age')
print(my_dict)

# access a particular element
print("Address :", my_dict.get('address'))

# remove all the elements
my_dict.clear()
print(my_dict)