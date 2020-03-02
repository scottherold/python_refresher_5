import shelve

# shelve files can be interacted with similar to dictionaries
# shelve file created liek a dictionary (must be closed however)
fruit = shelve.open("ShelfTest")

fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit grown in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])

# # shelve values can be reassigned like dictionary
# fruit["lime"] = "great with tequila"

# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break

#     if dict_key in fruit:
#         # add a default value if key not present
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# # shelve data is treated like a dicitonary
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

# shelve must be closed
fruit.close()