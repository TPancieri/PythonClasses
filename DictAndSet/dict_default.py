from contents import pantry

# the setdefault method returns the value of a key if the key exists in the dictionary
chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

# beans isn't in the pantry, so setdefault returns the default value specified, here its 0
beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

# the get method appears to be doing the same things as the setdefault method, the
# difference, though, is that set default doesn't just return the default value - it
# adds the key to the dictionary as well
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")
print()
print("`pantry` now contains....")

for key, value in sorted(pantry.items()):
    print(key, value)
