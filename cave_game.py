# Game boot
import shelve

# import data from shelves
locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')

# default location
loc = "1"

# game starts
# refactored to utilize nested dictionaries
while True:
    # creates available exits based on location
    availableExits = ", ".join(locations[loc]['exits'].keys())
    
    print(locations[loc]['desc'])

    # exit game, else combine both exits dictionaries
    if loc == "0":
        break
    else:
        # creates copy of the exits dictionary
        allExits = locations[loc]['exits'].copy()
        allExits.update(locations[loc]['namedExits'])
    
    # provides available exits
    direction = input("Avaible exits are " + availableExits+ " ").upper()
    print()

    # Parse user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            # will take the first word found in the user input, if in
            # the vocabulary dictionary
            if word in vocabulary:
                direction = vocabulary[word]
                break

    # check if directional key exists
    if direction in allExits:
        # coerced to string in order to use as shelve key
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

# closes shelves
vocabulary.close()
locations.close()