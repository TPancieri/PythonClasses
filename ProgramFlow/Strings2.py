# #                   1
# #         012345678901234
# parrot = "Norwegian Blue"
#
# print(parrot)
#
# print(parrot[3])
#
# for i in (4, 9, 3, 6, 8):
#     print(parrot[i])
#
# print()
#
# for i in (-11, -10, -5, -11, -8, -6):
#     print(parrot[i])
#
# print()
#
# print(parrot[0:9])
#
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:])
#
# print(parrot[0:6:2])
# print(parrot[0:6:3])    # third number is the step slice

# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

number = input("Please enter a series of numbers using any separators  you lke: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
