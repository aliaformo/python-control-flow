cities = ['new york city', 'mountain view', 'chicago', 'los angeles', 'houston']
for city in cities:
    print(city)
print("Done! \n")

'''new york city
mountain view
chicago
los angeles
houston
Done!'''


#----------------------------------------------------------------


for city in cities:
    print(city.title())
print("Done with titles!\n")


'''New York City
Mountain View
Chicago
Los Angeles
Houston
Done with titles!'''


#----------------------------------------------------------------


upper_cities=[]
for city in cities:
    upper_cities.append(city.upper())
print(upper_cities)
print("Done with upper cities!\n")

# ['NEW YORK CITY', 'MOUNTAIN VIEW', 'CHICAGO', 'LOS ANGELES', 'HOUSTON']
# Done with upper cities!



print(range(4)) # range(0, 4)

print(list(range(4))) # [0, 1, 2, 3]

print(list(range(2,8))) # [2, 3, 4, 5, 6, 7]

print(list(range(3,15, 3))) # [3, 6, 9, 12]

print(list(range(0, len(upper_cities)))) #  [0, 1, 2, 3, 4]


for index in range(len(cities)):
    cities[index] = cities[index].capitalize()
print(cities)

# ['New york city', 'Mountain view', 'Chicago', 'Los angeles', 'Houston']



