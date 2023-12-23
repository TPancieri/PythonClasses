from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict ."""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount
    # the setdefault method returns the value from the dictionary, if the key exits
    # if the key doesn't exist, it creates a new entry for the key, assigns the default
    # value to it, which is zero in this case, and then returns that default value.
    # we add amount to the value returned, then store the value back to the dictionary


# display_dict = {str(index + 1): meal for index. meal in enumerate(recipes)}
display_dict = {}
# creating an empty dictionary and iterating over its keys
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 25)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            # passing 0 as a default value if there's none of the item on pantry
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item}: OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
