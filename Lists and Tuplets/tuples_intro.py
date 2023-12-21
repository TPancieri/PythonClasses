albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981,),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

print(len(albums))


for name,artist,year in albums:
    print("Album: {} , Artist: {} , Year: {}"
          .format(name, artist, year))

# title, artist, year = albums
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)
#
