items = ['bananas', 'mattresses', 'dog kennels', 'machines', 'cheeses']
weights = [15,34,42,120, 5]

# with list
print('\nZip with list:')
print(list(zip(items, weights)))

# with for loop
print('\nZip with loops:')
for cargo in zip(items, weights):
    print(cargo[0], cargo[1])

#----------------------------------------------------------------
# unzip the list

manifest = [('bananas', 15), ('mattresses', 34),
            ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]

fruits, masses = zip(*manifest)

print('\nUnzip manifest list:')
print('Fruits', fruits)
print('Weights', masses)


#----------------------------------------------------------------

zipping = list(zip(['a', 'b', 'c', 'd', 'e'], [1,2,3,4,5]))
print('\nZipping, letters and numbers', zipping, '\n')

#----------------------------------------------------------------

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

#----------------------------------------------------------------
# In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letter, num = zip(*some_list)
print('letter list:', letter)  # letter list: ('a', 'b', 'c')
print('num list:', num) # num list: (1, 2, 3)

# ----------------------------------------------------------------

# Zip Coordinates
'''Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points.
Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.'''
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# write your for loop here
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    print(f'{label}: {x}, {y}, {z}')
    
'''F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1'''


#----------------------------------------------------------------
#Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights ))
print(cast)

# {'Barney': 72, 'Robin': 68, 'Ted': 72, 'Lily': 66, 'Marshall': 76}

#---------------------------------------------------------------
# Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = zip(*cast)
print(names) # ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
print(heights) # (72, 68, 72, 66, 76)


#----------------------------------------------------------------------
# Transpose with Zip
'''Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.'''
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose) # ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))



#-----------------------------------------------------------------
#-----------------------------------------------------------------

# Enumerate

for i, item in enumerate(items):
    print(i, item)

'''0 bananas
1 mattresses
2 dog kennels
3 machines
4 cheeses'''

animals = ['lion', 'dog', 'cat', 'bird']
for i, animal in enumerate(animals):
    print(i, animal)
    
'''0 lion
1 dog
2 cat
3 bird'''

#------------------------------------------------

dict_test = {'he': 'llo', 'good': 'morning', 'great':'night'}

for key, value in enumerate(dict_test):
    print(key, value)
    
'''0 he
1 good
2 great'''

# ----------------------------------------------------------------
#Enumerate
'''Use enumerate to modify the people list so that each element contains the name followed by the measure's corresponding height. For example, the first element of people should change from "Barney Stinson" to "Barney Stinson 72".'''

people = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
measures = [72, 68, 72, 66, 76]
for i, person in enumerate(people):
    people[i] = person + " " + str(measures[i])
print(people)
