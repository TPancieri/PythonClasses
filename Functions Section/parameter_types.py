# def func(p1, p2, *args, k, **kwargs):
#     print("positional-or-keyword:...{}, {}".format(p1, p2))
#     print("var-positional (*args):..{}".format(args))
#     print("keyword:.................{}".format(k))
#     print("var-keyword:.............{}".format(kwargs))
#
#
# func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)

def sum_numbers(*args: float) -> float:
    """ Sum of all the `numbers` passed through the arguments """
    value = 0
    for x in args:
        value += x
    return value


print(sum_numbers(8,20,2))
