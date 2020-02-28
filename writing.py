# fun with writing files
cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Syndney"]

# 'w' for writing
with open("cities.txt", 'w') as city_file:
    for city in cities:
        # print works for writing if you provide a .txt file
        # it just writes the the file, instead of the console
        print(city, file=city_file)

# grabbing information from a file, and generating a list (reverse of
# above process)

cities = []

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        # the strip() functions will remove the passed in argument from
        # the BEGINNING or END of a string
        cities.append(city.strip('\n'))

print(cities) # should print list of cities above, from written file
for city in cities:
    print(city)

# Sometimes Python can create/save a .txt. file, but it cannot read the
# file back in the same form

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
    (4, "Kentish Town Waltz"))

with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

# eval() can transform a string value into what Python determines to be
# the appropriate data type.
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for track in tracks:
    print(track)