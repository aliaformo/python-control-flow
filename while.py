card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())
print(hand)  # [10, 8]

# =================================================================
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
print(product)


# ----------------------------------------------------------------
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# write your for loop here
for num in range(2, number + 1):
    product *= num
print(product)


# ----------------------------------------------------------------

'''Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.'''

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

five_odds = 0
count = 0

for num in num_list:
    if num % 2 != 0 and count < 5:
        five_odds += num
        count += 1
print(five_odds)  # 993


# ===========================================================================
# Break

manifest = [('bananas', 15), ('mattresses', 34),
            ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]
weight = 0
items = []

for cargo in manifest:
    if weight >= 100:
        break
    else:
        items.append(cargo[0])
        weight += cargo[1]
print('Weight', weight)
print('Items', items)


# --------------------------------------------------------------------------------

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# Breaks the loop if weight is greater than or equal to the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


# ================================================================
'''Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs. Press the Run button from the top bar to run the code in a cell.'''



headlines = ["Local Bear Eaten by Man",
            "Legislature Announces New Laws",
            "Peasant Discovers Violence Inherent in System",
            "Cat Rescues Fireman Stuck in Tree",
            "Brave Knight Runs Away",
            "Paper book Review: Totally Traffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)


# --------------------------------------------------

## iterate through the check_prime list

check_prime = [23, 45,67,21,87,90,76,55,333,2,3,4,9,8,7]

for num in check_prime:

## check if the number is 2

    if num == 2:
        print("{} IS a prime number".format(num))
        continue

## search for factors, iterating through numbers ranging from 2 to the number itself

for i in range(2, num):

## number is not prime if modulo is 0

    if (num % i) == 0:
        print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
        break

## otherwise keep checking until we've searched all possible factors, and then declare it prime

    if i == num -1:    
        print("{} IS a prime number".format(num))