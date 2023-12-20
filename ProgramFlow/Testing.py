# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """

# Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isupper():
#         print(char)

# for i in range(0, 100, 7):
#     print(i)
#     if i % 11 == 0 and i != 0:
#         break

# number = 0
# while number < 20:
#     number += 1
#     if number % 3 != 0 and number % 5 != 0 and number != 0:
#         print(number)

# for value in range (11):
#     value = value * 2
#     print(value)
choice = None

while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break

    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")
