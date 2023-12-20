# program that asks for name and age
# check if the person is the right age to go to an 18-30 holiday , must be over 18 and under 31
# if they are welcome them to the holiday otherwise print a refusal

name = input("What's your name?")
age = int(input("How old are you? "))

if age <= 17 or age >= 31:
    print("Sorry {},because of you being {} you're not eligible to go on holiday".format(name, age))
else:
    print("Enjoy your holiday {} !".format(name))
