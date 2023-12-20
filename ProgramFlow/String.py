print("Today is a good day")
print('can we "quote" that?')
print("Hello " + "World")
greetings = "Hello"
name = input('Please enter your name')
# if we want a space , we add that too
print(greetings + ' ' + name)

age = 24
print(age)

print(type(greetings))
print(type(age))

age_in_words = "2 years"

# f string is defined by putting the letter f before the opening quotes
# then we can use a variable name inside curly braces, similar to replacement fields

print(name + f" is {age} years old")
print(type(age))

print(f"If Pi is approximately {22 / 7:12.50f} ")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
