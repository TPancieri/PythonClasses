age = 24
print("my age is {0} years ".format(age))

print("There are {0} days in {1}, {2},{3} ,{4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", " May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec"
      .format(31))

# Fields can appear more than once and they don`t have to appear in the order that the values are provided to the
# .format method call, its the index {the number inside the braces} that decides which value is going to be used

print("Jan: {2} , Fev: {0}, Mar: {2} , Apr: {1} , May: {2} , Jun: {1}"
      .format(28, 30, 31))

print()

print("""Jan: {2} 
Fev: {0}
Mar: {2} 
Apr: {1} 
May: {2} 
Jun: {1}""".format(28, 30, 31))
