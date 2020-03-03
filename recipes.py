import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# writeback allows you to modify data within the shelf, in a simple
# format. The trade-off is heavier memory usage
with shelve.open('recipes', writeback=True) as recipes:
    # recipes['blt'] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # # how to modify data in a shelve
    # just using .append() is not enough
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # # You need to set the shelved property to be a mutated property
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # with the writeback=True option, this will update the data simply
    # recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])