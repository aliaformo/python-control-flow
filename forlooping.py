# 1. Create Usernames
'''Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:'''

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# the usernames list should look like this:

["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ","_"))
print(usernames)

# ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']


# =================================================================

# 2. Modify Usernames with Range
'''Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.

After running your loop, this list'''

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")
print(usernames)

# ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']


# =================================================================

# 3. Tag Counter

'''Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.'''
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token.startswith("<") and token.endswith(">"): # if token[0] == '<' and token[-1] == '>':
        count+=1
print(count)

# 2

#==========================================================
# 4. Create an HTML List
'''Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is'''
items = ['first string', 'second string'], # printing html_str should output:'''

'''<ul>
<li>first string</li>
<li>second string</li>
</ul>'''

'''That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.'''

items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "    <li>{}</li>\n".format(item) # f'    <li>{item}</li>'
html_str += "</ul>"

print(html_str)

# <ul>
#     <li>first string</li>
#     <li>second string</li>
# </ul>




print(list(range(0,-5)))  # []