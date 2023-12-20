for i in range(1, 13):
    # : is the formatting
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # :< changes the alignment order , :^ makes it center
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))
# General format , 15 decimals

print("Pi is approximately {0:12f}".format(22/7))
# Specified using floating point, 6 digits after decimal point

print("Pi is approximately {0:12.50f}".format(22/7))
# Specified format with precision of 50, which giver 50 after decimal
# Python defines precision as more important the field width, does not truncate,
# ignores the value 12 that was specified for the width

print("Pi is approximately {0:52.50f}".format(22/7))
#

print("Pi is approximately {0:62.50f}".format(22/7))
#

print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

# Maximum precision of a floating point is between 51 and 53 digits

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}"
          .format(i, i ** 2, i ** 3))
