numbers = (0, 1, 2, 3, 4, 5)


# print(numbers)
# print(*numbers)

# star unpacks i.e. separates

def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
