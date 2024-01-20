# Method 1: Using a for loop to create a set of counters

book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
            'the', 'great', 'gatsby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

# Step 1: Create an empty dictionary.
word_counter = {}

# Step 2. Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1.

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gatsby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}


# =================================================================
# Method 2: Using the get method

word_get_counter = dict()

for word in book_title:
    word_get_counter[word] = word_get_counter.get(word, 0) + 1

print(word_get_counter)


# =======================================================================================

cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

# iterating only keys
for key in cast:
    print(key)


for key, value in cast.items():
    print(f'Actor: {key}  /   Role: {value}')


# =======================================================================================

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary

for item, quantity in basket_items.items():
    # if the key is in the list of fruits, add the value (number of fruits) to result
    if item in fruits:
        result += quantity
print(result)

# =======================================================================================
# Fruit Basket - Task 2

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for thing, amount in basket_items.items():
    if thing in fruits:
        fruit_count += amount
    else:
        not_fruit_count += amount
print(f'Fruits: {fruit_count}, No Fruits: {not_fruit_count}')
