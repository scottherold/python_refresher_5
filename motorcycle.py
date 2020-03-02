import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    # once the shelve is open, you can access it just like a dictionary
    for key in bike:
        print(key)
    
    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])