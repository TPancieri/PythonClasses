import copy
from contents import recipes


def my_deepcopy(dictionary: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values

    The function will crash with an AttributeError if the value aren't
    lists or dictionaries

    :param dictionary: The dictionary to copy
    :return: A copy of `dictionary`, with the values being copies of the
    original values

    """
    new_dict = {}
    for key, value in dictionary.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


animals = {
    "lion": ["scary", "big", "cat", ],
    "elephant": ["big", "grey", "wrinkled", ],
    "teddy": ["cuddly", "stuffed", ],
}

# Perform a shallow copy
# things = animals.copy()

# animals["teddy"] = "toy"

# Perform a deep copy
# things = copy.deepcopy(animals)
#
# print(id(things["teddy"]), things["teddy"])
# print(id(animals["teddy"]), animals["teddy"])
#
# print()
#
# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])

recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
