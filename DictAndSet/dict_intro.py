vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}
# dict. is {key:value} , use [] when retrieving a value

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", None)
# pop removes an item from the dictionary and returns the value
# if the key doesn't exist, it returns whatever you pass for the default instead
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# when you iterate over a dict you iterate the keys
# for key in vehicles:
#     print(key)
# if  you want the values you might decide to index the dictionary.
# for key in vehicles:
#     print(key, vehicles[key], sep=', ')
#          key , value
# the more efficient way of doing it is:
for key, value in vehicles.items():
    print(key, value, sep=", ")
# the .items method returns an iterator of tuples, and we unpack the tuples
# into our key and values variables, on line 30

# remember , enumerate when iterating over sequences ,and .items() when
# iterating over dictionaries
