menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "bacon", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# My solution
# for meal in menu:
#     for item in meal:
#         if item == "spam":
#             meal.remove(item)
#     print(meal)

# Class solution
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()
